
module logic_l5
  #(
    parameter PAR_DATA_BITS = 8
  )
  (
    input wire ib_clk,
    input wire ib_rst,
    
    input wire [PAR_DATA_BITS-1:0] ivG_data,
    output wire [PAR_DATA_BITS-1:0] ovG_data
  );

  reg [PAR_DATA_BITS-1:0] rvG_xor;

  always @(posedge ib_clk)
  begin
    if (ib_rst==1'b1)
    begin
      rvG_xor <= {PAR_DATA_BITS{1'b0}};
    end
    else
    begin
      rvG_xor <= rvG_xor ^ ivG_data;
    end
  end
  
  assign ovG_data = rvG_xor;

endmodule
