import 'dart:math' as math;

class VolumeCalculator {
  /// Calculate prostate volume and provide diagnosis
  /// 
  /// Parameters:
  /// - `dimensions`: List of 3 perpendicular diameters
  /// 
  /// Returns:
  /// - Formatted diagnosis string with volume and size assessment
  static String prostate(List<double> dimensions) {
    if (dimensions.length != 3) {
      throw ArgumentError('Prostate calculation requires exactly 3 dimensions');
    }
    
    double volume = ellipsoid(dimensions[0], dimensions[1], dimensions[2]);
    String diagnosis;
    
    if (volume < 25) {
      diagnosis = "Normal";
    } else if (volume == 25) {
      diagnosis = "Normal or Prominent";
    } else if (volume < 40) {
      diagnosis = "Prominent";
    } else if (volume == 40) {
      diagnosis = "Prominent or Enlarged";
    } else {
      diagnosis = "Enlarged";
    }
    
    return "$diagnosis size of prostate gland, measuring ${volume.round()} ml in volume.";
  }

  /// Calculate ellipsoid volume from 3 perpendicular diameters
  /// 
  /// Parameters:
  /// - `d1`: First diameter
  /// - `d2`: Second diameter  
  /// - `d3`: Third diameter
  /// 
  /// Returns:
  /// - Volume in cubic units
  static double ellipsoid(double d1, double d2, double d3) {
    return (4 / 3) * math.pi * (d1 / 2) * (d2 / 2) * (d3 / 2);
  }
}