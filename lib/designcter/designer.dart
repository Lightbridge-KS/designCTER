import 'package:flutter/services.dart' show rootBundle;
import 'package:mustachex/mustachex.dart';
import 'protocol.dart';
import '_utils.dart';

class Designer {
  final String protocolId;
  final Map<String, dynamic> parameters;
  
  Designer({
    required this.protocolId,
    this.parameters = const {},
  });

  Future<String> generate() async {
    // Check if it's MRI protocol
    if (protocolId == 'mri_screening_whole_spine') {
      return await designMR();
    } else {
      return await designCT();
    }
  }

  Future<String> designCT() async {
    // Get protocol info from the data structure
    final protocolInfo = ProtocolData.protocolInfo['ct']?[protocolId];
    if (protocolInfo == null) {
      throw Exception('Protocol ID not found: $protocolId');
    }

    // Load the mustache template
    final templateString = await rootBundle.loadString('lib/designcter/template/temp_ct.mustache');
    final template = Template(templateString, htmlEscapeValues: false);

    // Prepare data for template
    final data = _prepareCTData(protocolInfo);
    
    // Render template
    return template.renderString(data);
  }

  Future<String> designMR() async {
    // Get protocol info from the data structure
    final protocolInfo = ProtocolData.protocolInfo['mr']?[protocolId];
    if (protocolInfo == null) {
      throw Exception('Protocol ID not found: $protocolId');
    }

    // Load the mustache template
    final templateString = await rootBundle.loadString('lib/designcter/template/temp_mr.mustache');
    final template = Template(templateString, htmlEscapeValues: false);

    // Prepare data for template
    final data = _prepareMRData(protocolInfo);
    
    // Render template
    return template.renderString(data);
  }

  Map<String, dynamic> _prepareCTData(Map<String, Object> protocolInfo) {
    // Extract protocol information
    final examName = protocolInfo['examName'] as String?;
    final protocolName = protocolInfo['protocolName'];
    final phaseDesignText = protocolInfo['phaseDesignText'];
    final contrastText = protocolInfo['contrastText'] as String?;

    // Check if IV contrast is used from protocol data
    final useIVContrast = protocolInfo['useIVcontrast'] as bool? ?? false;

    // Get parameters with defaults
    final npoTime = dashIfBlank(parameters['npoTime'] ?? '');
    final egfrValue = dashIfBlank(parameters['egfrValue'] ?? '');
    final egfrDate = parameters['egfrDate'] ?? getCurrentDate();
    final renalPremed = dashIfBlank(parameters['renalPremed'] ?? '');
    final allergyPremed = dashIfBlank(parameters['allergyPremed'] ?? '');
    final pregnancy = boolYesDash(parameters['pregnancy'] ?? false);
    final hasETT = boolYesDash(parameters['hasETT'] ?? false);
    final hasC1 = boolYesDash(parameters['hasC1'] ?? false);
    final hasPrecaution = dashIfBlank(parameters['hasPrecaution'] ?? '');
    final specialInst = dashIfBlank(parameters['specialInst'] ?? '');
    final refPhysicianName = dashIfBlank(parameters['refPhysicianName'] ?? '');
    final refPhysicianTel = dashIfBlank(parameters['refPhysicianTel'] ?? '');

    // Build data map for mustache
    final data = <String, dynamic>{
      'hasETT': hasETT,
      'hasC1': hasC1,
      'hasPrecaution': hasPrecaution,
      'specialInst': specialInst,
      'refPhysicianName': refPhysicianName,
      'refPhysicianTel': refPhysicianTel,
    };

    // Add optional fields if they exist
    if (examName != null) {
      data['examName'] = examName;
    }

    if (protocolName != null && protocolName != false) {
      data['protocolName'] = protocolName;
    }

    if (phaseDesignText != null && phaseDesignText != false) {
      data['phaseDesignText'] = (phaseDesignText as String).trim();
    }

    if (contrastText != null) {
      data['contrastText'] = contrastText;
    }

    if (useIVContrast) {
      data['useIVcontrast'] = true;
      data['NPOtime'] = npoTime;
      data['eGFRdate'] = egfrDate;
      data['eGFRvalue'] = egfrValue;
      data['renalPremed'] = renalPremed;
      data['allergyPremed'] = allergyPremed;
      data['pregnancy'] = pregnancy;
    }

    return data;
  }

  Map<String, dynamic> _prepareMRData(Map<String, Object> protocolInfo) {
    // Extract protocol information
    final header = protocolInfo['header'] as String?;

    // Check if IV contrast is used from protocol data (for MRI it's Gd contrast)
    final useIVContrast = protocolInfo['useIVcontrast'] as bool? ?? false;

    // Get parameters with defaults
    final npoTime = dashIfBlank(parameters['npoTime'] ?? '');
    final egfrValue = dashIfBlank(parameters['egfrValue'] ?? '');
    final egfrDate = parameters['egfrDate'] ?? getCurrentDate();
    final renalPremed = dashIfBlank(parameters['renalPremed'] ?? '');
    final allergyPremed = dashIfBlank(parameters['allergyPremed'] ?? '');
    final pregnancy = boolYesDash(parameters['pregnancy'] ?? false);
    final hasETT = boolYesDash(parameters['hasETT'] ?? false);
    final hasC1 = boolYesDash(parameters['hasC1'] ?? false);
    final hasPrecaution = dashIfBlank(parameters['hasPrecaution'] ?? '');
    final specialInst = dashIfBlank(parameters['specialInst'] ?? '');
    final refPhysicianName = dashIfBlank(parameters['refPhysicianName'] ?? '');
    final refPhysicianTel = dashIfBlank(parameters['refPhysicianTel'] ?? '');

    // Build data map for mustache
    final data = <String, dynamic>{
      'header': header ?? '',
      'hasETT': hasETT,
      'hasC1': hasC1,
      'hasPrecaution': hasPrecaution,
      'specialInst': specialInst,
      'refPhysicianName': refPhysicianName,
      'refPhysicianTel': refPhysicianTel,
    };

    // Add contrast-related fields if IV contrast is used
    if (useIVContrast) {
      data['useIVcontrast'] = true;
      data['NPOtime'] = npoTime;
      data['eGFRdate'] = egfrDate;
      data['eGFRvalue'] = egfrValue;
      data['renalPremed'] = renalPremed;
      data['allergyPremed'] = allergyPremed;
      data['pregnancy'] = pregnancy;
    }

    return data;
  }
}