
`include "param.v"

module top
(
  input wire      ib_clk,
  input wire      [15:0] iv16_numA,
  input wire      [15:0] iv16_numB,
  input wire      [15:0] iv16_numC,
  output wire     [15:0] ov16_num
);
  inst `PAR_INST i_inst (
    .ib_clk(ib_clk),
    .iv16_numA(iv16_numA),
    .iv16_numB(iv16_numB),
    .iv16_numC(iv16_numC),
    .ov16_num(ov16_num)
  );

endmodule

