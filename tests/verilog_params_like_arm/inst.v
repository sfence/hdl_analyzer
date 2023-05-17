
`include "param.v"

module inst `PAR_DECL (
  input wire      ib_clk,
  input wire      [15:0] iv16_numA,
  input wire      [15:0] iv16_numB,
  input wire      [15:0] iv16_numC,
  output wire     [15:0] ov16_num
);

  localparam LPAR_A = PAR_A/16;
  localparam LPAR_B = PAR_B/16;
  localparam LPAR_C = PAR_C/16;
  reg    [47:0] rv48_numA, rv48_numB, rv48_numC;
  reg [15:0] rv16_num;
  
  always @(*)
  begin
    rv48_numA <= {48{1'b0}};
    rv48_numB <= {48{1'b0}};
    rv48_numC <= {48{1'b0}};
  
    rv48_numA[LPAR_A+15:LPAR_A] <= iv16_numA;
    rv48_numB[LPAR_B+15:LPAR_B] <= iv16_numB;
    rv48_numC[LPAR_C+15:LPAR_C] <= iv16_numC;
    
    rv48_numA[LPAR_A+31:LPAR_A+16] <= iv16_numA;
    rv48_numB[LPAR_B+31:LPAR_B+16] <= iv16_numB;
    rv48_numC[LPAR_C+31:LPAR_C+16] <= iv16_numC;
  end
  
  always @(posedge ib_clk)
  begin
    rv16_num <= rv48_numA[31:16] ^ rv48_numB[31:16] ^ rv48_numC[31:16];
  end
  
  assign ov16_num = rv16_num;

endmodule

