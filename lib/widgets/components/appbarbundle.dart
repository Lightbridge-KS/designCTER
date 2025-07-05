import 'package:flutter/material.dart';

/// A custom AppBar widget with integrated theme toggle functionality.
/// 
/// This widget provides a reusable AppBar with theme switching capabilities,
/// allowing customization of title and theme icons.
class AppBarBundle extends StatelessWidget implements PreferredSizeWidget {
  /// The title widget to display in the AppBar
  final Widget? title;
  
  /// Icon to display when in dark mode
  final IconData iconDark;
  
  /// Icon to display when in light mode
  final IconData iconLight;
  
  /// Current theme mode
  final ThemeMode themeMode;
  
  /// Callback function to toggle theme
  final VoidCallback onThemeToggle;

  const AppBarBundle({
    super.key,
    this.title,
    required this.iconDark,
    required this.iconLight,
    required this.themeMode,
    required this.onThemeToggle,
  });

  /// Get the appropriate theme icon based on current theme mode
  IconData _getThemeIcon() {
    // If system mode, check actual brightness
    if (themeMode == ThemeMode.system) {
      final brightness = WidgetsBinding.instance.platformDispatcher.platformBrightness;
      return brightness == Brightness.dark ? iconDark : iconLight;
    }
    
    // For explicit light/dark modes
    return themeMode == ThemeMode.dark ? iconDark : iconLight;
  }

  @override
  Widget build(BuildContext context) {
    return AppBar(
      title: title,
      backgroundColor: Theme.of(context).colorScheme.inversePrimary,
      leading: IconButton(
        icon: Icon(_getThemeIcon()),
        onPressed: onThemeToggle,
        tooltip: 'Toggle theme',
      ),
    );
  }

  @override
  Size get preferredSize => const Size.fromHeight(kToolbarHeight);
}