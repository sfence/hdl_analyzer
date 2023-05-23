
module xor_logic #
  (
    parameter PAR_DATA_BITS = 16,
    parameter PAR_XOR = 16'hA5A5
  )
  (
    input wire ib_clk,
    input wire ib_rst,
    
    input wire [PAR_DATA_BITS-1:0] ivG_data,
    output wire [PAR_DATA_BITS-1:0] ovG_data
  );
  
  reg [PAR_DATA_BITS-1:0] rvG_data;
 
  always @ (posedge ib_clk)
  begin
    if (ib_rst==1'b1) begin
      rvG_data <= PAR_XOR;
    end else begin
      rvG_data <= ivG_data ^ PAR_XOR;
    end
  end
  
  assign ovG_data = ivG_data ^ PAR_XOR;
  
endmodule 
