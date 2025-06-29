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
        expect(result1, contains('Routine WA')); // Should contain protocol name
      } catch (e) {
        print('Error: $e');
        fail('Designer failed to generate CT protocol: $e');
      }
    });

  });
}