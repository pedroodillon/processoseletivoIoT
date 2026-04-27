# Sistema de Inspeção Inteligente com Edge AI (IoT)

## 👤 Identificação
Nome: Pedro Odillon F. M. M. Figueiredo 
GitHub: pedroodillon

## 1️⃣ Visão Geral da Solução

Este projeto implementa um sistema embarcado de inspeção baseado no conceito de Edge AI aplicado à Indústria 4.0.

A solução foi desenvolvida em conjunto com um modelo de Inteligência Artificial (CNN treinada com MNIST), responsável pela etapa de **percepção**.

Neste projeto IoT, essa saída é simulada por um sinal analógico de um potenciômetro, representando a inferência do modelo embarcado.

O sistema realiza:

- Recebimento da saída da IA simulada
- Processamento local no ESP32
- Tomada de decisão em tempo real
- Atuação física por LEDs e buzzer

## 2️⃣ Arquitetura do Sistema Embarcado

O sistema segue um fluxo típico de aplicações embarcadas industriais:

```text
[ Modelo IA (CNN - MNIST) ]
↓
[ Inferência simulada via ADC ]
↓
[ Firmware ESP32 ]
↓
[ Decisão ]
↓
[ Atuadores: LEDs + buzzer ]
```

O firmware foi estruturado com uma máquina de estados:

- IDLE → Aguarda interação do usuário
- READ → Realiza leitura do sensor
- PROCESS → Interpreta o valor como saída da IA
- ACTUATE → Atualiza os atuadores

Essa abordagem melhora a organização, previsibilidade e manutenção do código.

## 3️⃣ Componentes Utilizados

- ESP32 simulado no Wokwi
- Botão como entrada digital
- Potenciômetro como entrada analógica via ADC
- LED verde para estado aprovado
- LED amarelo para estado de atenção
- LED vermelho para estado rejeitado
- Buzzer para alarme sonoro

## 4️⃣ Decisões Técnicas Relevantes

### Simulação da saída de IA

O potenciômetro foi utilizado para simular a saída de um modelo de IA, permitindo validar a lógica embarcada sem executar o modelo diretamente no hardware.

### Máquina de estados

A lógica foi organizada em estados bem definidos, evitando código monolítico e facilitando futuras melhorias.

### Separação de responsabilidades

O código foi dividido em funções para:

- leitura da entrada
- simulação de inferência
- tomada de decisão
- atualização dos atuadores

### Uso de ADC e PWM

O ADC foi utilizado para leitura do potenciômetro.  
O PWM foi utilizado para controle do buzzer.

## 5️⃣ Resultados Obtidos

O sistema apresentou os seguintes resultados:

- Leitura correta do valor analógico
- Classificação em três estados:
  - APPROVED
  - WARNING
  - REJECTED
- Acionamento correto dos LEDs e buzzer
- Execução estável na simulação do Wokwi
- Pipeline de CI/CD funcionando corretamente no GitHub Actions

## 6️⃣ Comentários Adicionais

### Integração com o desafio de IA

Este projeto representa a etapa de atuação de um sistema completo de Edge AI.

No projeto de IA, foi desenvolvido um modelo CNN para classificação e otimizado para TensorFlow Lite.

Neste projeto IoT:

- A saída do modelo é simulada via ADC
- O firmware interpreta essa saída
- O sistema toma decisões em tempo real
- Os atuadores refletem o resultado da classificação

Essa integração demonstra:

- IA → percepção e classificação
- IoT → decisão e atuação

### Contexto de aplicação

A solução pode ser aplicada em inspeção de qualidade, triagem automatizada e sistemas embarcados com inferência local.

### Limitações

- A inferência de IA foi simulada
- Não há comunicação externa como MQTT ou cloud
- A interface é limitada aos atuadores físicos

### Melhorias futuras

- Execução real do modelo TFLite no ESP32
- Adição de sensores como DHT22
- Uso de display I2C para telemetria
- Comunicação via MQTT
- Controle de servo motor para atuação física

## 🚀 Conclusão

O projeto demonstra a construção de um sistema embarcado funcional e organizado, integrando conceitos de IoT, automação e Edge AI, com aplicação direta em cenários da Indústria 4.0.