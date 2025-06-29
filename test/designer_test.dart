import 'package:flutter_test/flutter_test.dart';
import 'package:designcter/designcter/designer.dart';

void main() {
  // Set up a basic Flutter app context for testing
  setUpAll(() async {
    TestWidgetsFlutterBinding.ensureInitialized();
  });

  group('Designer Tests', () {
    testWidgets('Test 1: Basic CT protocol (ct_whole_abd_routine)', (WidgetTester tester) async {
      print('=== DesignCTER Quick Test ===\n');
      print('Test 1: Basic CT protocol (ct_whole_abd_routine)');
      print('-' * 50);
      
      try {
        final designer1 = Designer(protocolId: 'ct_whole_abd_routine');
        final result1 = await designer1.generate();
        print('Generated CT Protocol:');
        print(result1);
        print('\n' + '=' * 50);
        
        // Basic assertions
        expect(result1, isNotEmpty);
        expect(result1, contains('-')); // Should contain template content
      } catch (e) {
        print('Error: $e');
        fail('Designer failed to generate CT protocol: $e');
      }
    });

    testWidgets('Test 2: CT protocol with all parameters', (WidgetTester tester) async {
      print('Test 2: CT protocol with comprehensive parameters');
      print('-' * 50);
      
      try {
        final designer2 = Designer(
          protocolId: 'ct_whole_abd_routine',
          npoTime: '6 hours',
          egfrDate: 'June 29, 2025',
          egfrValue: '85',
          renalPremed: 'N-acetylcysteine 600mg PO bid',
          allergyPremed: 'Prednisolone 50mg PO + Diphenhydramine 50mg IV',
          pregnancy: false,
          hasETT: true,
          hasC1: false,
          hasPrecaution: 'Patient has pacemaker',
          specialInst: 'Include delayed images if positive',
          refPhysicianName: 'Dr. Smith',
          refPhysicianTel: '02-123-4567',
        );
        final result2 = await designer2.generate();
        print('Generated CT Protocol with Parameters:');
        print(result2);
        print('\n' + '=' * 50);
        
        // Comprehensive assertions
        expect(result2, isNotEmpty);
        expect(result2, contains('6 hours')); // NPO time
        expect(result2, contains('85')); // eGFR value
        expect(result2, contains('Dr. Smith')); // Physician name
        expect(result2, contains('Yes')); // ET tube status
        expect(result2, contains('Patient has pacemaker')); // Precaution
        
      } catch (e) {
        print('Error: $e');
        fail('Designer failed to generate CT protocol with parameters: $e');
      }
    });

    testWidgets('Test 3: MRI protocol (mri_screening_whole_spine)', (WidgetTester tester) async {
      print('Test 3: MRI protocol (mri_screening_whole_spine)');
      print('-' * 50);
      
      try {
        final designer3 = Designer(
          protocolId: 'mri_screening_whole_spine',
          hasETT: false,
          hasC1: true,
          hasPrecaution: 'Claustrophobic - may need sedation',
          refPhysicianName: 'Dr. Johnson',
        );
        final result3 = await designer3.generate();
        print('Generated MRI Protocol:');
        print(result3);
        print('\n' + '=' * 50);
        
        // MRI-specific assertions
        expect(result3, isNotEmpty);
        expect(result3, contains('MRI')); // Should contain MRI content
        expect(result3, contains('Dr. Johnson')); // Physician name
        expect(result3, contains('Yes')); // C1 status
        expect(result3, contains('Claustrophobic')); // Precaution
        
      } catch (e) {
        print('Error: $e');
        fail('Designer failed to generate MRI protocol: $e');
      }
    });

    testWidgets('Test 4: CTA protocol (cta_pe_no_dvt)', (WidgetTester tester) async {
      print('Test 4: CTA protocol (cta_pe_no_dvt)');
      print('-' * 50);
      
      try {
        final designer4 = Designer(
          protocolId: 'cta_pe_no_dvt',
          npoTime: '4 hours',
          egfrValue: '95',
          pregnancy: false,
          refPhysicianName: 'Dr. Wilson',
        );
        final result4 = await designer4.generate();
        print('Generated CTA Protocol:');
        print(result4);
        print('\n' + '=' * 50);
        
        // CTA-specific assertions
        expect(result4, isNotEmpty);
        expect(result4, contains('4 hours')); // NPO time
        expect(result4, contains('95')); // eGFR value
        expect(result4, contains('Dr. Wilson')); // Physician name
        
      } catch (e) {
        print('Error: $e');
        fail('Designer failed to generate CTA protocol: $e');
      }
    });

    test('Test 5: Invalid protocol ID should throw exception', () async {
      print('Test 5: Invalid protocol ID handling');
      print('-' * 50);
      
      final designer5 = Designer(protocolId: 'invalid_protocol_id');
      
      expect(
        () async => await designer5.generate(),
        throwsException,
      );
      
      print('✓ Exception correctly thrown for invalid protocol ID\n');
      print('=' * 50);
    });

    test('Test 6: Constructor parameter validation', () {
      print('Test 6: Constructor parameter validation');
      print('-' * 50);
      
      // Test required parameter
      expect(
        () => Designer(protocolId: 'ct_whole_abd_routine'),
        returnsNormally,
      );
      
      // Test with optional parameters
      expect(
        () => Designer(
          protocolId: 'ct_whole_abd_routine',
          npoTime: '6 hours',
          pregnancy: true,
        ),
        returnsNormally,
      );
      
      print('✓ Constructor parameters validated successfully\n');
      print('=' * 50);
    });
  });
}