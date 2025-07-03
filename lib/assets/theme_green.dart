import "package:flutter/material.dart";

class MaterialTheme {
  final TextTheme textTheme;

  const MaterialTheme(this.textTheme);

  static ColorScheme lightScheme() {
    return const ColorScheme(
      brightness: Brightness.light,
      primary: Color(0xff4c662b),
      surfaceTint: Color(0xff4c662b),
      onPrimary: Color(0xffffffff),
      primaryContainer: Color(0xffcdeda3),
      onPrimaryContainer: Color(0xff354e16),
      secondary: Color(0xff586249),
      onSecondary: Color(0xffffffff),
      secondaryContainer: Color(0xffdce7c8),
      onSecondaryContainer: Color(0xff404a33),
      tertiary: Color(0xff386663),
      onTertiary: Color(0xffffffff),
      tertiaryContainer: Color(0xffbcece7),
      onTertiaryContainer: Color(0xff1f4e4b),
      error: Color(0xffba1a1a),
      onError: Color(0xffffffff),
      errorContainer: Color(0xffffdad6),
      onErrorContainer: Color(0xff93000a),
      surface: Color(0xfff9faef),
      onSurface: Color(0xff1a1c16),
      onSurfaceVariant: Color(0xff44483d),
      outline: Color(0xff75796c),
      outlineVariant: Color(0xffc5c8ba),
      shadow: Color(0xff000000),
      scrim: Color(0xff000000),
      inverseSurface: Color(0xff2f312a),
      inversePrimary: Color(0xffb1d18a),
      primaryFixed: Color(0xffcdeda3),
      onPrimaryFixed: Color(0xff102000),
      primaryFixedDim: Color(0xffb1d18a),
      onPrimaryFixedVariant: Color(0xff354e16),
      secondaryFixed: Color(0xffdce7c8),
      onSecondaryFixed: Color(0xff151e0b),
      secondaryFixedDim: Color(0xffbfcbad),
      onSecondaryFixedVariant: Color(0xff404a33),
      tertiaryFixed: Color(0xffbcece7),
      onTertiaryFixed: Color(0xff00201e),
      tertiaryFixedDim: Color(0xffa0d0cb),
      onTertiaryFixedVariant: Color(0xff1f4e4b),
      surfaceDim: Color(0xffdadbd0),
      surfaceBright: Color(0xfff9faef),
      surfaceContainerLowest: Color(0xffffffff),
      surfaceContainerLow: Color(0xfff3f4e9),
      surfaceContainer: Color(0xffeeefe3),
      surfaceContainerHigh: Color(0xffe8e9de),
      surfaceContainerHighest: Color(0xffe2e3d8),
    );
  }

  ThemeData light() {
    return theme(lightScheme());
  }

  static ColorScheme lightMediumContrastScheme() {
    return const ColorScheme(
      brightness: Brightness.light,
      primary: Color(0xff253d05),
      surfaceTint: Color(0xff4c662b),
      onPrimary: Color(0xffffffff),
      primaryContainer: Color(0xff5a7539),
      onPrimaryContainer: Color(0xffffffff),
      secondary: Color(0xff303924),
      onSecondary: Color(0xffffffff),
      secondaryContainer: Color(0xff667157),
      onSecondaryContainer: Color(0xffffffff),
      tertiary: Color(0xff083d3a),
      onTertiary: Color(0xffffffff),
      tertiaryContainer: Color(0xff477572),
      onTertiaryContainer: Color(0xffffffff),
      error: Color(0xff740006),
      onError: Color(0xffffffff),
      errorContainer: Color(0xffcf2c27),
      onErrorContainer: Color(0xffffffff),
      surface: Color(0xfff9faef),
      onSurface: Color(0xff0f120c),
      onSurfaceVariant: Color(0xff34382d),
      outline: Color(0xff505449),
      outlineVariant: Color(0xff6b6f62),
      shadow: Color(0xff000000),
      scrim: Color(0xff000000),
      inverseSurface: Color(0xff2f312a),
      inversePrimary: Color(0xffb1d18a),
      primaryFixed: Color(0xff5a7539),
      onPrimaryFixed: Color(0xffffffff),
      primaryFixedDim: Color(0xff425c23),
      onPrimaryFixedVariant: Color(0xffffffff),
      secondaryFixed: Color(0xff667157),
      onSecondaryFixed: Color(0xffffffff),
      secondaryFixedDim: Color(0xff4e5840),
      onSecondaryFixedVariant: Color(0xffffffff),
      tertiaryFixed: Color(0xff477572),
      onTertiaryFixed: Color(0xffffffff),
      tertiaryFixedDim: Color(0xff2e5c59),
      onTertiaryFixedVariant: Color(0xffffffff),
      surfaceDim: Color(0xffc6c7bd),
      surfaceBright: Color(0xfff9faef),
      surfaceContainerLowest: Color(0xffffffff),
      surfaceContainerLow: Color(0xfff3f4e9),
      surfaceContainer: Color(0xffe8e9de),
      surfaceContainerHigh: Color(0xffdcded3),
      surfaceContainerHighest: Color(0xffd1d3c8),
    );
  }

  ThemeData lightMediumContrast() {
    return theme(lightMediumContrastScheme());
  }

  static ColorScheme lightHighContrastScheme() {
    return const ColorScheme(
      brightness: Brightness.light,
      primary: Color(0xff1c3200),
      surfaceTint: Color(0xff4c662b),
      onPrimary: Color(0xffffffff),
      primaryContainer: Color(0xff375018),
      onPrimaryContainer: Color(0xffffffff),
      secondary: Color(0xff262f1a),
      onSecondary: Color(0xffffffff),
      secondaryContainer: Color(0xff434c35),
      onSecondaryContainer: Color(0xffffffff),
      tertiary: Color(0xff003230),
      onTertiary: Color(0xffffffff),
      tertiaryContainer: Color(0xff21504e),
      onTertiaryContainer: Color(0xffffffff),
      error: Color(0xff600004),
      onError: Color(0xffffffff),
      errorContainer: Color(0xff98000a),
      onErrorContainer: Color(0xffffffff),
      surface: Color(0xfff9faef),
      onSurface: Color(0xff000000),
      onSurfaceVariant: Color(0xff000000),
      outline: Color(0xff2a2d24),
      outlineVariant: Color(0xff474b40),
      shadow: Color(0xff000000),
      scrim: Color(0xff000000),
      inverseSurface: Color(0xff2f312a),
      inversePrimary: Color(0xffb1d18a),
      primaryFixed: Color(0xff375018),
      onPrimaryFixed: Color(0xffffffff),
      primaryFixedDim: Color(0xff213903),
      onPrimaryFixedVariant: Color(0xffffffff),
      secondaryFixed: Color(0xff434c35),
      onSecondaryFixed: Color(0xffffffff),
      secondaryFixedDim: Color(0xff2c3620),
      onSecondaryFixedVariant: Color(0xffffffff),
      tertiaryFixed: Color(0xff21504e),
      onTertiaryFixed: Color(0xffffffff),
      tertiaryFixedDim: Color(0xff033937),
      onTertiaryFixedVariant: Color(0xffffffff),
      surfaceDim: Color(0xffb8baaf),
      surfaceBright: Color(0xfff9faef),
      surfaceContainerLowest: Color(0xffffffff),
      surfaceContainerLow: Color(0xfff1f2e6),
      surfaceContainer: Color(0xffe2e3d8),
      surfaceContainerHigh: Color(0xffd4d5ca),
      surfaceContainerHighest: Color(0xffc6c7bd),
    );
  }

  ThemeData lightHighContrast() {
    return theme(lightHighContrastScheme());
  }

  static ColorScheme darkScheme() {
    return const ColorScheme(
      brightness: Brightness.dark,
      primary: Color(0xffb1d18a),
      surfaceTint: Color(0xffb1d18a),
      onPrimary: Color(0xff1f3701),
      primaryContainer: Color(0xff354e16),
      onPrimaryContainer: Color(0xffcdeda3),
      secondary: Color(0xffbfcbad),
      onSecondary: Color(0xff2a331e),
      secondaryContainer: Color(0xff404a33),
      onSecondaryContainer: Color(0xffdce7c8),
      tertiary: Color(0xffa0d0cb),
      onTertiary: Color(0xff003735),
      tertiaryContainer: Color(0xff1f4e4b),
      onTertiaryContainer: Color(0xffbcece7),
      error: Color(0xffffb4ab),
      onError: Color(0xff690005),
      errorContainer: Color(0xff93000a),
      onErrorContainer: Color(0xffffdad6),
      surface: Color(0xff12140e),
      onSurface: Color(0xffe2e3d8),
      onSurfaceVariant: Color(0xffc5c8ba),
      outline: Color(0xff8f9285),
      outlineVariant: Color(0xff44483d),
      shadow: Color(0xff000000),
      scrim: Color(0xff000000),
      inverseSurface: Color(0xffe2e3d8),
      inversePrimary: Color(0xff4c662b),
      primaryFixed: Color(0xffcdeda3),
      onPrimaryFixed: Color(0xff102000),
      primaryFixedDim: Color(0xffb1d18a),
      onPrimaryFixedVariant: Color(0xff354e16),
      secondaryFixed: Color(0xffdce7c8),
      onSecondaryFixed: Color(0xff151e0b),
      secondaryFixedDim: Color(0xffbfcbad),
      onSecondaryFixedVariant: Color(0xff404a33),
      tertiaryFixed: Color(0xffbcece7),
      onTertiaryFixed: Color(0xff00201e),
      tertiaryFixedDim: Color(0xffa0d0cb),
      onTertiaryFixedVariant: Color(0xff1f4e4b),
      surfaceDim: Color(0xff12140e),
      surfaceBright: Color(0xff383a32),
      surfaceContainerLowest: Color(0xff0c0f09),
      surfaceContainerLow: Color(0xff1a1c16),
      surfaceContainer: Color(0xff1e201a),
      surfaceContainerHigh: Color(0xff282b24),
      surfaceContainerHighest: Color(0xff33362e),
    );
  }

  ThemeData dark() {
    return theme(darkScheme());
  }

  static ColorScheme darkMediumContrastScheme() {
    return const ColorScheme(
      brightness: Brightness.dark,
      primary: Color(0xffc7e79e),
      surfaceTint: Color(0xffb1d18a),
      onPrimary: Color(0xff172b00),
      primaryContainer: Color(0xff7d9a59),
      onPrimaryContainer: Color(0xff000000),
      secondary: Color(0xffd5e1c2),
      onSecondary: Color(0xff1f2814),
      secondaryContainer: Color(0xff8a9579),
      onSecondaryContainer: Color(0xff000000),
      tertiary: Color(0xffb5e6e1),
      onTertiary: Color(0xff002b29),
      tertiaryContainer: Color(0xff6b9995),
      onTertiaryContainer: Color(0xff000000),
      error: Color(0xffffd2cc),
      onError: Color(0xff540003),
      errorContainer: Color(0xffff5449),
      onErrorContainer: Color(0xff000000),
      surface: Color(0xff12140e),
      onSurface: Color(0xffffffff),
      onSurfaceVariant: Color(0xffdbdecf),
      outline: Color(0xffb0b3a6),
      outlineVariant: Color(0xff8e9285),
      shadow: Color(0xff000000),
      scrim: Color(0xff000000),
      inverseSurface: Color(0xffe2e3d8),
      inversePrimary: Color(0xff364f17),
      primaryFixed: Color(0xffcdeda3),
      onPrimaryFixed: Color(0xff081400),
      primaryFixedDim: Color(0xffb1d18a),
      onPrimaryFixedVariant: Color(0xff253d05),
      secondaryFixed: Color(0xffdce7c8),
      onSecondaryFixed: Color(0xff0b1403),
      secondaryFixedDim: Color(0xffbfcbad),
      onSecondaryFixedVariant: Color(0xff303924),
      tertiaryFixed: Color(0xffbcece7),
      onTertiaryFixed: Color(0xff001413),
      tertiaryFixedDim: Color(0xffa0d0cb),
      onTertiaryFixedVariant: Color(0xff083d3a),
      surfaceDim: Color(0xff12140e),
      surfaceBright: Color(0xff43453d),
      surfaceContainerLowest: Color(0xff060804),
      surfaceContainerLow: Color(0xff1c1e18),
      surfaceContainer: Color(0xff262922),
      surfaceContainerHigh: Color(0xff31342c),
      surfaceContainerHighest: Color(0xff3c3f37),
    );
  }

  ThemeData darkMediumContrast() {
    return theme(darkMediumContrastScheme());
  }

  static ColorScheme darkHighContrastScheme() {
    return const ColorScheme(
      brightness: Brightness.dark,
      primary: Color(0xffdafbb0),
      surfaceTint: Color(0xffb1d18a),
      onPrimary: Color(0xff000000),
      primaryContainer: Color(0xffadcd86),
      onPrimaryContainer: Color(0xff050e00),
      secondary: Color(0xffe9f4d5),
      onSecondary: Color(0xff000000),
      secondaryContainer: Color(0xffbcc7a9),
      onSecondaryContainer: Color(0xff060d01),
      tertiary: Color(0xffc9f9f5),
      onTertiary: Color(0xff000000),
      tertiaryContainer: Color(0xff9cccc7),
      onTertiaryContainer: Color(0xff000e0d),
      error: Color(0xffffece9),
      onError: Color(0xff000000),
      errorContainer: Color(0xffffaea4),
      onErrorContainer: Color(0xff220001),
      surface: Color(0xff12140e),
      onSurface: Color(0xffffffff),
      onSurfaceVariant: Color(0xffffffff),
      outline: Color(0xffeef2e2),
      outlineVariant: Color(0xffc1c4b6),
      shadow: Color(0xff000000),
      scrim: Color(0xff000000),
      inverseSurface: Color(0xffe2e3d8),
      inversePrimary: Color(0xff364f17),
      primaryFixed: Color(0xffcdeda3),
      onPrimaryFixed: Color(0xff000000),
      primaryFixedDim: Color(0xffb1d18a),
      onPrimaryFixedVariant: Color(0xff081400),
      secondaryFixed: Color(0xffdce7c8),
      onSecondaryFixed: Color(0xff000000),
      secondaryFixedDim: Color(0xffbfcbad),
      onSecondaryFixedVariant: Color(0xff0b1403),
      tertiaryFixed: Color(0xffbcece7),
      onTertiaryFixed: Color(0xff000000),
      tertiaryFixedDim: Color(0xffa0d0cb),
      onTertiaryFixedVariant: Color(0xff001413),
      surfaceDim: Color(0xff12140e),
      surfaceBright: Color(0xff4f5149),
      surfaceContainerLowest: Color(0xff000000),
      surfaceContainerLow: Color(0xff1e201a),
      surfaceContainer: Color(0xff2f312a),
      surfaceContainerHigh: Color(0xff3a3c35),
      surfaceContainerHighest: Color(0xff454840),
    );
  }

  ThemeData darkHighContrast() {
    return theme(darkHighContrastScheme());
  }


  ThemeData theme(ColorScheme colorScheme) => ThemeData(
     useMaterial3: true,
     brightness: colorScheme.brightness,
     colorScheme: colorScheme,
     textTheme: textTheme.apply(
       bodyColor: colorScheme.onSurface,
       displayColor: colorScheme.onSurface,
     ),
     scaffoldBackgroundColor: colorScheme.background,
     canvasColor: colorScheme.surface,
  );

  /// Custom Color 1
  static const customColor1 = ExtendedColor(
    seed: Color(0xff64ac44),
    value: Color(0xff64ac44),
    light: ColorFamily(
      color: Color(0xff446832),
      onColor: Color(0xffffffff),
      colorContainer: Color(0xffc4efac),
      onColorContainer: Color(0xff2d4f1d),
    ),
    lightMediumContrast: ColorFamily(
      color: Color(0xff446832),
      onColor: Color(0xffffffff),
      colorContainer: Color(0xffc4efac),
      onColorContainer: Color(0xff2d4f1d),
    ),
    lightHighContrast: ColorFamily(
      color: Color(0xff446832),
      onColor: Color(0xffffffff),
      colorContainer: Color(0xffc4efac),
      onColorContainer: Color(0xff2d4f1d),
    ),
    dark: ColorFamily(
      color: Color(0xffa9d292),
      onColor: Color(0xff163808),
      colorContainer: Color(0xff2d4f1d),
      onColorContainer: Color(0xffc4efac),
    ),
    darkMediumContrast: ColorFamily(
      color: Color(0xffa9d292),
      onColor: Color(0xff163808),
      colorContainer: Color(0xff2d4f1d),
      onColorContainer: Color(0xffc4efac),
    ),
    darkHighContrast: ColorFamily(
      color: Color(0xffa9d292),
      onColor: Color(0xff163808),
      colorContainer: Color(0xff2d4f1d),
      onColorContainer: Color(0xffc4efac),
    ),
  );

  /// Custom Color 2
  static const customColor2 = ExtendedColor(
    seed: Color(0xff182941),
    value: Color(0xff182941),
    light: ColorFamily(
      color: Color(0xff3d5f90),
      onColor: Color(0xffffffff),
      colorContainer: Color(0xffd5e3ff),
      onColorContainer: Color(0xff234776),
    ),
    lightMediumContrast: ColorFamily(
      color: Color(0xff3d5f90),
      onColor: Color(0xffffffff),
      colorContainer: Color(0xffd5e3ff),
      onColorContainer: Color(0xff234776),
    ),
    lightHighContrast: ColorFamily(
      color: Color(0xff3d5f90),
      onColor: Color(0xffffffff),
      colorContainer: Color(0xffd5e3ff),
      onColorContainer: Color(0xff234776),
    ),
    dark: ColorFamily(
      color: Color(0xffa6c8ff),
      onColor: Color(0xff02315f),
      colorContainer: Color(0xff234776),
      onColorContainer: Color(0xffd5e3ff),
    ),
    darkMediumContrast: ColorFamily(
      color: Color(0xffa6c8ff),
      onColor: Color(0xff02315f),
      colorContainer: Color(0xff234776),
      onColorContainer: Color(0xffd5e3ff),
    ),
    darkHighContrast: ColorFamily(
      color: Color(0xffa6c8ff),
      onColor: Color(0xff02315f),
      colorContainer: Color(0xff234776),
      onColorContainer: Color(0xffd5e3ff),
    ),
  );


  List<ExtendedColor> get extendedColors => [
    customColor1,
    customColor2,
  ];
}

class ExtendedColor {
  final Color seed, value;
  final ColorFamily light;
  final ColorFamily lightHighContrast;
  final ColorFamily lightMediumContrast;
  final ColorFamily dark;
  final ColorFamily darkHighContrast;
  final ColorFamily darkMediumContrast;

  const ExtendedColor({
    required this.seed,
    required this.value,
    required this.light,
    required this.lightHighContrast,
    required this.lightMediumContrast,
    required this.dark,
    required this.darkHighContrast,
    required this.darkMediumContrast,
  });
}

class ColorFamily {
  const ColorFamily({
    required this.color,
    required this.onColor,
    required this.colorContainer,
    required this.onColorContainer,
  });

  final Color color;
  final Color onColor;
  final Color colorContainer;
  final Color onColorContainer;
}
