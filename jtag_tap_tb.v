/*
 * Testbench for JTAG TAP module
 * Test functionality of JTAG TAP
 */

module jtag_tap_tb ();

	/* Parameter */
	localparam WIDTH = 8; /* Set to 8-bits for simplicity */

	/* Inputs and outputs of the jtag_tap.v file */
	reg TCK, TMS, TDI, TRST;
	reg [WIDTH-1:0] socOutput;

	wire TDO, socCLK, socRST, socTestSel;

jtag_tap #(.WIDTH(WIDTH)) TAP_UUT (.TCK(TCK), .TMS(TMS), .TDI(TDI), .TRST(TRST), .socOutput(socOutput), .TDO(TDO), .socCLK(socCLK), .socRST(socRST), .socTestSel(socTestSel));

initial
begin

	/* Initial clock state */
	TCK <= 0;
	
	/* Test reset */
	TRST <= 1;
	TDI <= 1;
	TMS <= 0;
	socOutput <= 122;
	#10;

	/* Test shift register load */
	TRST <= 0;
	TDI <= 1;
	TMS <= 1;
	socOutput <= 212;
	#10;
	TMS <= 0;
	#100;

	$stop;

end

always
begin

	#5 TCK <= ~TCK;

end

endmodule
