/*
 * Testbench for shift register module
 * Testing correct functionality in shift register
 */

module shift_register_tb();

	/* Parameter definition for shift register length */
	localparam SHFT_LENGTH = 8; /* Testing 8-bits for simplicity */
	
	/* Input and output signals declared as regs or wires */
	reg clk, rst, load;
	reg [SHFT_LENGTH-1:0] socOutput;

	wire jtagOutput;

/* Create instance of the shift register module to test */
shift_register #(.LENGTH(SHFT_LENGTH)) SHFT_REG_UUT (.clk(clk), .rst(rst), .load(load), .socOutput(socOutput), .jtagOutput(jtagOutput));

/* Begin testing */
initial
begin
	
	/* Define initial clock state */
	clk <= 0;
	
	/* Test for reset conditions */
	rst <= 1;
	load <= 1;
	socOutput <= 132;
	#10;

	/* Check for data load */
	rst <= 0;
	load <= 1;
	socOutput <= 83;
	#10;

	/* Test for shifting */
	rst <= 0;
	load <= 0;
	socOutput <= 165;
	#100;

	$stop;

end

/* Always block for clock generation */
always
begin

	#5 clk <= ~clk;

end

endmodule
