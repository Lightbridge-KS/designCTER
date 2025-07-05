import 'package:flutter/material.dart';
import 'package:flutter/foundation.dart';
// Conditional imports - only import window_manager on non-web platforms
import 'window_manager_stub.dart' if (dart.library.io) 'package:window_manager/window_manager.dart';

import 'assets/theme_brown.dart';
// import 'assets/theme_green.dart';
// import 'assets/theme_blue.dart';
import 'widgets/design/page_protocol_design.dart';
import 'widgets/page_calculator.dart';


void main() async {

  WidgetsFlutterBinding.ensureInitialized(); 
  
  // Only configure window manager for desktop platforms
  if (!kIsWeb) {
    await initializeWindow();
  }
  runApp(const MainApp());
}

class MainApp extends StatefulWidget {
  const MainApp({super.key});

  @override
  State<MainApp> createState() => _MainAppState();
}

class _MainAppState extends State<MainApp> {
  ThemeMode _themeMode = ThemeMode.system;
  int _currentPageIndex = 0;

  void _toggleTheme() {
    setState(() {
      switch (_themeMode) {
        case ThemeMode.system:
          // If system, check current brightness and toggle to opposite
          final brightness = WidgetsBinding.instance.platformDispatcher.platformBrightness;
          _themeMode = brightness == Brightness.dark ? ThemeMode.light : ThemeMode.dark;
          break;
        case ThemeMode.light:
          _themeMode = ThemeMode.dark;
          break;
        case ThemeMode.dark:
          _themeMode = ThemeMode.light;
          break;
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    final materialTheme = MaterialTheme(Theme.of(context).textTheme);
    
    return MaterialApp(
      title: 'DesignCTER',
      theme: materialTheme.light(),
      darkTheme: materialTheme.dark(),
      themeMode: _themeMode,
      home: Scaffold(
        body: IndexedStack(
          index: _currentPageIndex,
          children: [
            ProtocolDesignPage(
              themeMode: _themeMode,
              onThemeToggle: _toggleTheme,
            ),
            CalculatorPage(
              themeMode: _themeMode,
              onThemeToggle: _toggleTheme,
            ),
          ],
        ),
        bottomNavigationBar: NavigationBar(
          selectedIndex: _currentPageIndex,
          onDestinationSelected: (index) {
            setState(() {
              _currentPageIndex = index;
            });
          },
          destinations: const [
            NavigationDestination(
              icon: Icon(Icons.brush_rounded),
              label: 'Design',
            ),
            NavigationDestination(
              icon: Icon(Icons.calculate_rounded),
              label: 'Calculate',
            ),
          ],
        ),
      ),
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