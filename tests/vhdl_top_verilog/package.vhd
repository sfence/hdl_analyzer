
package PACK_verilog
  component verilog_abc_xor is
    port (
      ib_clk  : in  std_logic;
      ib_a    : in  std_logic;
      ib_nb   : in  std_logic;
      ib_c    : in  std_logic;
      ob_xor  : out std_logic;
    );
  end component;
end package;

