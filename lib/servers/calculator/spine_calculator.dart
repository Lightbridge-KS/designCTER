import '_statistics.dart';
import '_parser.dart';

/// Calculator for spine height loss and compression fracture assessment
class SpineCalculator {
  
  /// Calculates spine height loss from string inputs
  ///
  /// Parameters
  /// ----------
  /// normalCm : String representation of normal vertebral heights
  /// collapsedCM : String representation of collapsed vertebral heights
  ///
  /// Returns
  /// -------
  /// String
  ///     Formatted string with compression fracture diagnosis and height loss percentage
  ///
  /// Throws
  /// ------
  /// ArgumentError
  ///     If string inputs cannot be parsed to valid numbers
  static String spineHeightLossFromString({required String normalCm, required String collapsedCM}) {
    // Parse normal heights
    dynamic normalParsed = parseStrToNumOrList(normalCm);
    if (normalParsed == "") {
      return "";
    }
    
    // Parse collapsed heights
    dynamic collapsedParsed = parseStrToNumOrList(collapsedCM);
    if (collapsedParsed == "") {
      return "";
    }
    
    // Convert to lists for consistency
    List<double> normalList = normalParsed is double ? [normalParsed] : normalParsed;
    List<double> collapsedList = collapsedParsed is double ? [collapsedParsed] : collapsedParsed;
    
    // Call existing method
    return spineHeightLoss(normalCm: normalList, collapsedCM: collapsedList);
  }


  /// Calculates spine height loss percentage and provides diagnostic assessment
  ///
  /// Parameters
  /// ----------
  /// normalCm : List of normal vertebral heights in centimeters
  /// collapsedCM : List of collapsed vertebral heights in centimeters
  ///
  /// Returns
  /// -------
  /// String
  ///     Formatted string with compression fracture diagnosis and height loss percentage
  ///
  /// Throws
  /// ------
  /// ArgumentError
  ///     If collapsed height is greater than normal height (negative loss)
  static String spineHeightLoss({required List<double> normalCm, required List<double> collapsedCM}) {
    // Calculate mean if input as list
    double normalMean = Statistics.mean(normalCm);
    double collapsedMean = Statistics.mean(collapsedCM);
    
    // Calculate loss percentage
    double lossPercent = ((normalMean - collapsedMean) / normalMean) * 100;
    if (lossPercent < 0) {
      return "";
    }
    
    // Get diagnosis
    String diagnosis = _spineHeightLossDx(lossPercent: lossPercent);
    
    // Format output
    return "$diagnosis compression fracture (${lossPercent.round()}% height loss).";
  }

  /// Determines compression fracture severity based on height loss percentage
  ///
  /// Parameters
  /// ----------
  /// lossPercent : double
  ///     Percentage of height loss
  ///
  /// Returns
  /// -------
  /// String
  ///     Severity classification of compression fracture
  ///
  /// Throws
  /// ------
  /// ArgumentError
  ///     If loss percentage is negative
  static String _spineHeightLossDx({required double lossPercent}) {
    // Negative case
    if (lossPercent < 0) {
      throw ArgumentError("`collapsedCM` must be less than `normalCm`");
    }
    
    String diagnosis;
    if (lossPercent < 20) {
      diagnosis = "Less than mild";
    } else if (lossPercent < 25) {
      diagnosis = "Mild";
    } else if (lossPercent == 25) {
      diagnosis = "Mild to moderate";
    } else if (lossPercent < 40) {
      diagnosis = "Moderate";
    } else if (lossPercent == 40) {
      diagnosis = "Moderate to severe";
    } else {
      diagnosis = "Severe";
    }
    
    return diagnosis;
  }
}