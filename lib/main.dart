import 'package:flutter/material.dart';
import 'package:flutter/foundation.dart';
// Conditional imports - only import window_manager on non-web platforms
import 'window_manager_stub.dart' if (dart.library.io) 'package:window_manager/window_manager.dart';


import 'widgets/page_protocol_design.dart';


void main() async {

  WidgetsFlutterBinding.ensureInitialized(); 
  
  // Only configure window manager for desktop platforms
  if (!kIsWeb) {
    await initializeWindow();
  }
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


// Window initialization function that only runs on desktop
Future<void> initializeWindow() async {
  if (!kIsWeb) {
    await windowManager.ensureInitialized(); 

    WindowOptions windowOptions = const WindowOptions(
      size: Size(840, 840), // Set your desired initial size
      center: true,
      backgroundColor: Colors.transparent,
      skipTaskbar: false,
      titleBarStyle: TitleBarStyle.normal,
    );
    windowManager.setMinimumSize(Size(840, 840));
    windowManager.waitUntilReadyToShow(windowOptions, () async {
      await windowManager.show();
      await windowManager.focus();
    });
  }
}