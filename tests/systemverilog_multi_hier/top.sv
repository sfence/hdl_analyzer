
`include "params.sv"

module top
  (
    input wire ib_clk,
    input wire ib_rst,
    
    input wire [`PAR_GLB_DATA_BITS-1:0] ivG_data,
    output wire [`PAR_GLB_DATA_BITS-1:0] ovG_data
  );
  
  genvar g_N;
      
  wire [15:0] wvG_data [0:`PAR_GLB_DATA_BITS/16-1];
  
  generate
    for (g_N = 16; g_N < `PAR_GLB_DATA_BITS; g_N = g_N + 16)
    begin
      logic_l1 #(
          .PAR_DATA_BITS(16)
        ) i_logic_l1 (
          .ib_clk(ib_clk),
          .ib_rst(ib_rst),
          
          .ivG_data(ivG_data[g_N-1:g_N-16]),
          .ovG_data(wvG_data[g_N/16])
        );
      assign ovG_data[g_N-1:g_N-16] = wvG_data[g_N/16];
    end
  endgenerate
endmodule
