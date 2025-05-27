```mermaid
graph TD
  encode --> step1
  encode --> step2
  encode --> step3
  encode --> step4
  encode --> step5

  step1 --> step1_dec
  step2 --> step2_dec
  step3 --> step3_dec
  step4 --> step4_dec
  step5 --> step5_dec

  step1 -->|ASCII vowels| ascii_logic
  step5 -->|regex transform| regex_handling
