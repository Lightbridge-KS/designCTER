import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import '../designcter/designer.dart';
import 'input_design.dart';
import 'components/appbarbundle.dart';

class ProtocolDesignPage extends StatefulWidget {
  final ThemeMode themeMode;
  final VoidCallback onThemeToggle;
  
  const ProtocolDesignPage({
    super.key,
    required this.themeMode,
    required this.onThemeToggle,
  });

  @override
  State<ProtocolDesignPage> createState() => _ProtocolDesignPageState();
}

class _ProtocolDesignPageState extends State<ProtocolDesignPage> {
  final GlobalKey<InputDesignState> _inputDesignKey = GlobalKey<InputDesignState>();
  final TextEditingController _outputController = TextEditingController();
  
  // State to hold current input values
  Map<String, dynamic> _currentInputs = {};

  // Check if all required selections are complete
  bool get _isSelectionComplete {
    return _currentInputs['protocolId'] != null;
  }

  @override
  void dispose() {
    _outputController.dispose();
    super.dispose();
  }

  /// Generate protocol template
  Future<void> _generateProtocol() async {
    if (!_isSelectionComplete) {
      _showSnackBar('Please select a protocol first');
      return;
    }

    try {
      final designer = Designer(
        protocolId: _currentInputs['protocolId'],
        npoTime: _currentInputs['npoTime'],
        egfrDate: _currentInputs['egfrDate'],
        egfrValue: _currentInputs['egfrValue'],
        renalPremed: _currentInputs['renalPremed'],
        allergyPremed: _currentInputs['allergyPremed'],
        pregnancy: _currentInputs['pregnancy'],
        hasETT: _currentInputs['hasETT'],
        hasC1: _currentInputs['hasC1'],
        hasPrecaution: _currentInputs['hasPrecaution'],
        specialInst: _currentInputs['specialInst'],
        refPhysicianName: _currentInputs['refPhysicianName'],
        refPhysicianTel: _currentInputs['refPhysicianTel'],
      );

      final template = await designer.generate();
      
      setState(() {
        _outputController.text = template;
      });
      
    } catch (e) {
      _showSnackBar('Error generating protocol: $e');
    }
  }

  /// Reset all inputs
  void _resetInputs() {
    _inputDesignKey.currentState?.reset();
    setState(() {
      _outputController.clear();
      _currentInputs = {};
    });
  }

  /// Copy output to clipboard
  Future<void> _copyToClipboard() async {
    if (_outputController.text.isNotEmpty) {
      await Clipboard.setData(ClipboardData(text: _outputController.text));
      _showSnackBar('Copied to clipboard');
    }
  }

  /// Show snackbar message
  void _showSnackBar(String message) {
    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(content: Text(message)),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBarBundle(
        title: const Text('Design CTER Protocol', style: TextStyle(fontWeight: FontWeight.bold)),
        iconDark: Icons.dark_mode_outlined,
        iconLight: Icons.brightness_5,
        themeMode: widget.themeMode,
        onThemeToggle: widget.onThemeToggle,
      ),
      body: LayoutBuilder(
        builder: (context, constraints) {
          // Use responsive layout
          if (constraints.maxWidth > 800) {
            // Desktop layout - side by side
            return _buildDesktopLayout();
          } else {
            // Mobile layout - stacked
            return _buildMobileLayout();
          }
        },
      ),
    );
  }

  Widget _buildDesktopLayout() {
    return SingleChildScrollView(
      padding: const EdgeInsets.all(16.0),
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          // Left side - Input form
          Expanded(
            flex: 1,
            child: Card(
              child: Padding(
                padding: const EdgeInsets.all(16.0),
                child: InputDesign(
                  key: _inputDesignKey,
                  onSelectionChanged: (inputs) {
                    setState(() {
                      _currentInputs = inputs;
                    });
                  },
                ),
              ),
            ),
          ),
          
          const SizedBox(width: 16),
          
          // Right side - Output and buttons
          Expanded(
            flex: 1,
            child: _buildOutputSection(),
          ),
        ],
      ),
    );
  }

  Widget _buildMobileLayout() {
    return SingleChildScrollView(
      padding: const EdgeInsets.all(16.0),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          // Input form
          Card(
            child: Padding(
              padding: const EdgeInsets.all(16.0),
              child: InputDesign(
                key: _inputDesignKey,
                onSelectionChanged: (inputs) {
                  setState(() {
                    _currentInputs = inputs;
                  });
                },
              ),
            ),
          ),
          
          const SizedBox(height: 16),
          
          // Output and buttons
          _buildOutputSection(),
        ],
      ),
    );
  }

  Widget _buildOutputSection() {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        // Output text field
        Card(
          child: Padding(
            padding: const EdgeInsets.all(16.0),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                TextField(
                  controller: _outputController,
                  maxLines: 23,
                  readOnly: false,
                  decoration: const InputDecoration(
                    border: OutlineInputBorder(),
                    focusedBorder: OutlineInputBorder(
                      borderSide: BorderSide(color: Colors.deepPurple),
                    ),
                    hintText: 'Generated protocol will appear here...',
                  ),
                  style: const TextStyle(
                    fontFamily: 'monospace',
                    fontSize: 14,
                  ),
                ),
              ],
            ),
          ),
        ),
        
        const SizedBox(height: 16),
        
        // Buttons
        Row(
          mainAxisAlignment: MainAxisAlignment.spaceBetween,
          children: [
            // Generate and Copy buttons
            Row(
              children: [
                ElevatedButton.icon(
                  onPressed: _isSelectionComplete ? _generateProtocol : null,
                  icon: const Icon(Icons.create),
                  label: const Text('Generate'),
                  style: ElevatedButton.styleFrom(
                    backgroundColor: Colors.grey[300],
                    foregroundColor: Colors.black87,
                    ),
                ),
                const SizedBox(width: 8),
                IconButton(
                  onPressed: _outputController.text.isNotEmpty ? _copyToClipboard : null,
                  icon: const Icon(Icons.copy),
                  tooltip: 'Copy to clipboard',
                ),
              ],
            ),
            
            // Reset button
            ElevatedButton.icon(
              onPressed: _resetInputs,
              icon: const Icon(Icons.refresh),
              label: const Text('Reset'),
            ),
          ],
        ),
      ],
    );
  }
}
