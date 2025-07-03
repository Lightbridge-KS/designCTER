import 'package:flutter/material.dart';
import 'designcter/protocol.dart';
import 'widgets/dropdowns_three.dart';

void main() {
  runApp(const MainApp());
}

class MainApp extends StatelessWidget {
  const MainApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'DesignCTER',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.blue),
        useMaterial3: true,
      ),
      home: const ProtocolDesignPage(),
    );
  }
}

class ProtocolDesignPage extends StatefulWidget {
  const ProtocolDesignPage({super.key});

  @override
  State<ProtocolDesignPage> createState() => _ProtocolDesignPageState();
}

class _ProtocolDesignPageState extends State<ProtocolDesignPage> {
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
        title: const Text('DesignCTER'),
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            
            // The three-level dropdowns component
            ThreeLevelDropdowns(
              choiceIdMap: ProtocolData.choiceIdMap,
              idDispMap: ProtocolData.idDispMap,
              onSelectionChanged: (selectionMap) {
                setState(() {
                  _protocolSelection = selectionMap;
                });
                // For Debug:
                // Print selections to console for debugging
                // print('=== Protocol Selection Debug ===');
                // print('Category ID: ${selectionMap['level1']}');
                // print('Exam ID: ${selectionMap['level2']}');
                // print('Protocol ID: ${selectionMap['level3']}');
                // print('Category Name: ${_getDisplayName(selectionMap['level1'])}');
                // print('Exam Name: ${_getDisplayName(selectionMap['level2'])}');
                // print('Protocol Name: ${_getDisplayName(selectionMap['level3'])}');
                // print('Selection Complete: $_isSelectionComplete');
                // print('================================');
              },
            ),

          ],
        ),
      ),
    );
  }

  /// Builds the selection display card
  
}
