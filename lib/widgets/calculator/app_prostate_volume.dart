import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import '../../servers/calculator/volume_calculator.dart';
import '../components/buttons.dart';

class AppProstateVolumeCalculator extends StatefulWidget {
  const AppProstateVolumeCalculator({super.key});

  @override
  State<AppProstateVolumeCalculator> createState() => _AppProstateVolumeCalculatorState();
}

class _AppProstateVolumeCalculatorState extends State<AppProstateVolumeCalculator> {
  final TextEditingController _inputController = TextEditingController();
  final TextEditingController _outputController = TextEditingController();

  @override
  void dispose() {
    _inputController.dispose();
    _outputController.dispose();
    super.dispose();
  }

  void _calculate() {
    final result = VolumeCalculator.prostateFromString(_inputController.text);
    setState(() {
      _outputController.text = result;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(
          'Prostate Volume',
          style: Theme.of(context).textTheme.headlineSmall?.copyWith(
            fontWeight: FontWeight.bold,
          ),
        ),
        const SizedBox(height: 16),
        Row(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Expanded(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  TextField(
                    controller: _inputController,
                    decoration: const InputDecoration(
                      labelText: 'Diameters in 3 planes (cm)',
                      hintText: 'e.g. 4.4 4.5 4.6',
                      border: OutlineInputBorder(),
                    ),
                    onSubmitted: (_) => _calculate(),
                  ),
                  const SizedBox(height: 8),
                  Text(
                    'Input perpendicular diameters (cm) in 3 planes, separated by spaces or comma (e.g. 4.4 4.5 4.6)',
                    style: Theme.of(context).textTheme.bodySmall?.copyWith(
                      color: Colors.grey,
                    ),
                  ),
                  const SizedBox(height: 4),
                  Text(
                    'Normal (<25 ml), Prominent (25-40 ml), Enlarged (>40 ml)',
                    style: Theme.of(context).textTheme.bodySmall?.copyWith(
                      color: Colors.grey,
                    ),
                  ),
                ],
              ),
            ),
            const SizedBox(width: 16),
            Expanded(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  TextField(
                    controller: _outputController,
                    decoration: const InputDecoration(
                      labelText: 'Prostate Volume',
                      border: OutlineInputBorder(),
                    ),
                    readOnly: false,
                  ),
                  const SizedBox(height: 8),
                  Row(
                    children: [
                      GenerateButton(onPressed: _calculate),
                      const SizedBox(width: 8),
                      CopyButton(controller: _outputController),
                    ],
                  ),
                ],
              ),
            ),
          ],
        ),
      ],
    );
  }
}