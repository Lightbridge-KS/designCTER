import 'package:flutter/material.dart';
import 'designcter/protocol.dart';
import 'widgets/dropdowns_three.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'DesignCTER',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.blue),
        useMaterial3: true,
      ),
      home: const ProtocolSelectorPage(),
    );
  }
}

class ProtocolSelectorPage extends StatefulWidget {
  const ProtocolSelectorPage({super.key});

  @override
  State<ProtocolSelectorPage> createState() => _ProtocolSelectorPageState();
}

class _ProtocolSelectorPageState extends State<ProtocolSelectorPage> {
  // State to hold the dropdown selections
  Map<String, String?> _protocolSelection = {
    'level1': null, // Category
    'level2': null, // Exam
    'level3': null, // Protocol
  };

  // Helper method to get display name from ID
  String _getDisplayName(String? id) {
    if (id == null) return 'Not selected';
    return ProtocolData.idDispMap[id] ?? id;
  }

  // Check if all selections are complete
  bool get _isSelectionComplete {
    return _protocolSelection['level1'] != null &&
           _protocolSelection['level2'] != null &&
           _protocolSelection['level3'] != null;
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('DesignCTER - Protocol Selector'),
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            // Header
            const Text(
              'CT Protocol Template Generator',
              style: TextStyle(
                fontSize: 28,
                fontWeight: FontWeight.bold,
              ),
            ),
            const SizedBox(height: 8),
            
            // The three-level dropdowns component
            ThreeLevelDropdowns(
              choiceIdMap: ProtocolData.choiceIdMap,
              idDispMap: ProtocolData.idDispMap,
              onSelectionChanged: (selectionMap) {
                setState(() {
                  _protocolSelection = selectionMap;
                });
                // Print selections to console for debugging
                print('=== Protocol Selection Debug ===');
                print('Category ID: ${selectionMap['level1']}');
                print('Exam ID: ${selectionMap['level2']}');
                print('Protocol ID: ${selectionMap['level3']}');
                print('Category Name: ${_getDisplayName(selectionMap['level1'])}');
                print('Exam Name: ${_getDisplayName(selectionMap['level2'])}');
                print('Protocol Name: ${_getDisplayName(selectionMap['level3'])}');
                print('Selection Complete: $_isSelectionComplete');
                print('================================');
              },
            ),

            const SizedBox(height: 32),

            // Selection display section
            if (_protocolSelection['level1'] != null) ...[
              _buildSelectionDisplay(),
              const SizedBox(height: 24),
            ],

            // Action buttons
            _buildActionButtons(),
          ],
        ),
      ),
    );
  }

  /// Builds the selection display card
  Widget _buildSelectionDisplay() {
    return Card(
      elevation: 2,
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(
              children: [
                Icon(
                  _isSelectionComplete ? Icons.check_circle : Icons.radio_button_unchecked,
                  color: _isSelectionComplete ? Colors.green : Colors.orange,
                ),
                const SizedBox(width: 8),
                Text(
                  _isSelectionComplete ? 'Selection Complete' : 'Selection in Progress',
                  style: TextStyle(
                    fontSize: 18,
                    fontWeight: FontWeight.w600,
                    color: _isSelectionComplete ? Colors.green : Colors.orange,
                  ),
                ),
              ],
            ),
            const SizedBox(height: 16),
            _buildSelectionRow('Category', _protocolSelection['level1']),
            _buildSelectionRow('Exam', _protocolSelection['level2']),
            _buildSelectionRow('Protocol', _protocolSelection['level3']),
            
            if (_isSelectionComplete) ...[
              const SizedBox(height: 16),
              Container(
                width: double.infinity,
                padding: const EdgeInsets.all(12),
                decoration: BoxDecoration(
                  color: Colors.green.shade50,
                  borderRadius: BorderRadius.circular(8),
                  border: Border.all(color: Colors.green.shade200),
                ),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    const Text(
                      'Selected Protocol:',
                      style: TextStyle(
                        fontWeight: FontWeight.w600,
                        fontSize: 14,
                      ),
                    ),
                    const SizedBox(height: 4),
                    Text(
                      '${_getDisplayName(_protocolSelection['level3'])} (${_getDisplayName(_protocolSelection['level2'])}, ${_getDisplayName(_protocolSelection['level1'])})',
                      style: const TextStyle(
                        fontSize: 16,
                        fontWeight: FontWeight.w500,
                      ),
                    ),
                  ],
                ),
              ),
            ],
          ],
        ),
      ),
    );
  }

  /// Helper to build individual selection rows
  Widget _buildSelectionRow(String label, String? valueId) {
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 4),
      child: Row(
        children: [
          SizedBox(
            width: 100,
            child: Text(
              '$label:',
              style: const TextStyle(
                fontWeight: FontWeight.w500,
                fontSize: 16,
              ),
            ),
          ),
          Expanded(
            child: Text(
              _getDisplayName(valueId),
              style: TextStyle(
                fontSize: 16,
                color: valueId != null ? Colors.black : Colors.grey,
                fontStyle: valueId != null ? FontStyle.normal : FontStyle.italic,
              ),
            ),
          ),
        ],
      ),
    );
  }

  /// Builds action buttons section
  Widget _buildActionButtons() {
    return Row(
      children: [
        Expanded(
          child: ElevatedButton.icon(
            onPressed: () {
              setState(() {
                _protocolSelection = {
                  'level1': null,
                  'level2': null,
                  'level3': null,
                };
              });
              print('=== Protocol Selection Reset ===');
            },
            icon: const Icon(Icons.refresh),
            label: const Text('Reset'),
            style: ElevatedButton.styleFrom(
              padding: const EdgeInsets.symmetric(vertical: 12),
            ),
          ),
        ),
        const SizedBox(width: 12),
        Expanded(
          child: ElevatedButton.icon(
            onPressed: _isSelectionComplete ? () => _generateProtocol() : null,
            icon: const Icon(Icons.description),
            label: const Text('Generate Template'),
            style: ElevatedButton.styleFrom(
              padding: const EdgeInsets.symmetric(vertical: 12),
            ),
          ),
        ),
      ],
    );
  }

  /// Handle protocol generation
  void _generateProtocol() {
    showDialog(
      context: context,
      builder: (context) => AlertDialog(
        title: const Text('Protocol Template Generated'),
        content: Column(
          mainAxisSize: MainAxisSize.min,
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const Text('Selected protocol:'),
            const SizedBox(height: 8),
            Text(
              'Category: ${_getDisplayName(_protocolSelection['level1'])}',
              style: const TextStyle(fontWeight: FontWeight.w500),
            ),
            Text(
              'Exam: ${_getDisplayName(_protocolSelection['level2'])}',
              style: const TextStyle(fontWeight: FontWeight.w500),
            ),
            Text(
              'Protocol: ${_getDisplayName(_protocolSelection['level3'])}',
              style: const TextStyle(fontWeight: FontWeight.w500),
            ),
            const SizedBox(height: 12),
            const Text(
              'Template generation will be implemented in the next steps.',
              style: TextStyle(fontStyle: FontStyle.italic),
            ),
          ],
        ),
        actions: [
          TextButton(
            onPressed: () => Navigator.of(context).pop(),
            child: const Text('OK'),
          ),
        ],
      ),
    );
  }
}
