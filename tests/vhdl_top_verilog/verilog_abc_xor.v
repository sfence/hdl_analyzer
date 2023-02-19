
module verilog_abc_xor(
    input wire ib_clk,
    input wire ib_a,
    input wire ib_nb,
    input wire ib_c,
    output wire ob_xor
  );

  reg rb_xor = 1'b0;
  
  always (posedge(ib_clk):
    rb_xor = ib_a ^ (~ib_nb) ^ ib_c;
  end
  
  assign ob_xor = rb_xor;

endmodule

