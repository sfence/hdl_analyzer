
entity top is
  port(
    ib_clk: std_logic;
    iv6_xor: std_logic_vector(1 downto 0);
    ov2_xor: std_logic_vector(1 downto 0)
  );
end top;

architecture rtl of top is
begin
  
  i_xor_1 : verilog_abc_xor
    port map(
      ib_clk => ib_clk,
      ib_a => iv6_xor(0),
      ib_nb => iv6_xor(1),
      ib_c => iv6_xor(2),
      ob_xor => ov2_xor(0)
    );
  i_xor_2 : verilog_abc_xor
    port map(
      ib_clk => ib_clk,
      ib_a => iv6_xor(3),
      ib_nb => iv6_xor(4),
      ib_c => iv6_xor(5),
      ob_xor => ov2_xor(0)
    );
end rtl;
