
module logic_l2
  #(
    parameter PAR_DATA_BITS = 8
  )
  (
    input wire ib_clk,
    input wire ib_rst,
    
    input wire [PAR_DATA_BITS-1:0] ivG_data,
    output wire [PAR_DATA_BITS-1:0] ovG_data
  );

  reg [PAR_DATA_BITS-1:0] rvG_sum;
  wire [PAR_DATA_BITS-1:0] wvG_xor;


  always @(posedge ib_clk)
  begin
    if (ib_rst==1'b1)
    begin
      rvG_sum <= {PAR_DATA_BITS{1'b0}};
    end
    else
    begin
      rvG_sum <= rvG_sum + ivG_data;
    end
  end
  
  logic_l3
    #(
      .PAR_DATA_BITS(PAR_DATA_BITS/2)
    ) i_logic_l3_a (
      .ib_clk(ib_clk),
      .ib_rst(ib_rst),
      .ivG_data(rvG_sum[PAR_DATA_BITS/2-1:0]),
      .ovG_data(wvG_xor[PAR_DATA_BITS-1:PAR_DATA_BITS/2])
    );
  logic_l3
    #(
      .PAR_DATA_BITS(PAR_DATA_BITS/2)
    ) i_logic_l3_b (
      .ib_clk(ib_clk),
      .ib_rst(ib_rst),
      .ivG_data(rvG_sum[PAR_DATA_BITS-1:PAR_DATA_BITS/2]),
      .ovG_data(wvG_xor[PAR_DATA_BITS/2-1:0])
    );
  
  assign ovG_data = rvG_sum ^ wvG_xor;

endmodule
