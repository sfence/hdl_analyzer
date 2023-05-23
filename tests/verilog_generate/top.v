

`include "params.v"

module top
  (
    input wire ib_clk,
    input wire ib_rst,
    
    input wire [15:0] ivG_data,
    output wire [15:0] ovG_data
  );
  
  genvar g_N;
      
  wire [15:0] wvG_data [0:3];
  
  cond #(
      .PAR_IF_A(1),
      .PAR_IF_B(0),
      .PAR_IF_C(0),
      .PAR_XOR_A(16'h0F0F),
      .PAR_XOR_B(16'hF0F0),
      .PAR_XOR_C(16'h0F0F),
      .PAR_XOR_D(16'h0F0F),
      .PAR_DATA_BITS(16)
    ) i_cond_100 (
      .ib_clk(ib_clk),
      .ib_rst(ib_rst),
      
      .ivG_data(ivG_data),
      .ovG_data(wvG_data[0])
    );
  generate
    if (`MAC_COND_IF_A) begin
      cond #(
          .PAR_IF_A(0),
          .PAR_IF_B(1),
          .PAR_IF_C(0),
          .PAR_XOR_A(16'h0F0F),
          .PAR_XOR_B(16'hF0F0),
          .PAR_XOR_C(16'h0F0F),
          .PAR_XOR_D(16'h0F0F),
          .PAR_DATA_BITS(16)
        ) i_cond_010 (
          .ib_clk(ib_clk),
          .ib_rst(ib_rst),
          
          .ivG_data(wvG_data[0]),
          .ovG_data(wvG_data[1])
        );
    end
  endgenerate
  generate
    if (`MAC_COND_IF_B) begin
      cond #(
          .PAR_IF_A(0),
          .PAR_IF_B(0),
          .PAR_IF_C(1),
          .PAR_XOR_A(16'h0F0F),
          .PAR_XOR_B(16'hF0F0),
          .PAR_XOR_C(16'h0F0F),
          .PAR_XOR_D(16'h0F0F),
          .PAR_DATA_BITS(16)
        ) i_cond_001 (
          .ib_clk(ib_clk),
          .ib_rst(ib_rst),
          
          .ivG_data(wvG_data[1]),
          .ovG_data(wvG_data[2])
        );
    end else begin
      assign wvG_data[2] = (`MAC_COND_IF_A)?wvG_data[1]:wvG_data[0];
    end
  endgenerate
  cond #(
      .PAR_IF_A(0),
      .PAR_IF_B(0),
      .PAR_IF_C(0),
      .PAR_XOR_A(16'h0F0F),
      .PAR_XOR_B(16'hF0F0),
      .PAR_XOR_C(16'h0F0F),
      .PAR_XOR_D(16'h0F0F),
      .PAR_DATA_BITS(16)
    ) i_cond_000 (
      .ib_clk(ib_clk),
      .ib_rst(ib_rst),
      
      .ivG_data(wvG_data[2]),
      .ovG_data(wvG_data[3])
    );
  
  assign ovG_data = wvG_data[3];
endmodule

