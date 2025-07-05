import 'package:flutter/material.dart';
import 'components/appbarbundle.dart';

class CalculatorPage extends StatefulWidget {
  final ThemeMode themeMode;
  final VoidCallback onThemeToggle;
  
  const CalculatorPage({
    super.key,
    required this.themeMode,
    required this.onThemeToggle,
  });

  @override
  State<CalculatorPage> createState() => _CalculatorPageState();
}

class _CalculatorPageState extends State<CalculatorPage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBarBundle(
        title: const Text('Radiology Calculator', style: TextStyle(fontWeight: FontWeight.bold)),
        iconDark: Icons.dark_mode_outlined,
        iconLight: Icons.brightness_5,
        themeMode: widget.themeMode,
        onThemeToggle: widget.onThemeToggle,
      ),
      body: const Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Icon(
              Icons.calculate_rounded,
              size: 64,
              color: Colors.grey,
            ),
            SizedBox(height: 16),
            Text(
              'Radiology Calculator Page',
              style: TextStyle(
                fontSize: 24,
                fontWeight: FontWeight.bold,
                color: Colors.grey,
              ),
            ),
            SizedBox(height: 8),
            Text(
              'Coming Soon...',
              style: TextStyle(
                fontSize: 16,
                color: Colors.grey,
              ),
            ),
          ],
        ),
      ),
    );
  }
}