
module cond #
  (
    parameter PAR_IF_A = 1,
    parameter PAR_IF_B = 0,
    parameter PAR_IF_C = 0,
    parameter PAR_XOR_A = 16'h0F0F,
    parameter PAR_XOR_B = 16'hF0F0,
    parameter PAR_XOR_C = 16'h0F0F,
    parameter PAR_XOR_D = 16'h0F0F,
    parameter PAR_DATA_BITS = 16
  )
  (
    input wire ib_clk,
    input wire ib_rst,
    
    input wire [PAR_DATA_BITS-1:0] ivG_data,
    output wire [PAR_DATA_BITS-1:0] ovG_data
  );
  
  generate
    if (PAR_IF_A==1) 
    begin
      xor_logic #(
          .PAR_DATA_BITS(PAR_DATA_BITS),
          .PAR_XOR(PAR_XOR_A)
        ) i_logic_A (
          .ib_clk(ib_clk),
          .ib_rst(ib_rst),
          
          .ivG_data(ivG_data),
          .ovG_data(ovG_data)
        );
    end else if (PAR_IF_B==1) begin
      xor_logic #(
          .PAR_DATA_BITS(PAR_DATA_BITS),
          .PAR_XOR(PAR_XOR_B)
        ) i_logic_B (
          .ib_clk(ib_clk),
          .ib_rst(ib_rst),
          
          .ivG_data(ivG_data),
          .ovG_data(ovG_data)
        );
    end else if (PAR_IF_C==1) begin
      xor_logic #(
          .PAR_DATA_BITS(PAR_DATA_BITS),
          .PAR_XOR(PAR_XOR_C)
        ) i_logic_C (
          .ib_clk(ib_clk),
          .ib_rst(ib_rst),
          
          .ivG_data(ivG_data),
          .ovG_data(ovG_data)
        );
    end else begin
      xor_logic #(
          .PAR_DATA_BITS(PAR_DATA_BITS),
          .PAR_XOR(PAR_XOR_D)
        ) i_logic_D (
          .ib_clk(ib_clk),
          .ib_rst(ib_rst),
          
          .ivG_data(ivG_data),
          .ovG_data(ovG_data)
        );
    end
  endgenerate
endmodule

