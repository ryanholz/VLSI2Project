/*
 * JTAG Test Access Port module
 *
 * JTAG Ports:
 * - TCK: Test Clock
 * - TMS: Test Mode Select. Additional control for JTAG.
 * - TDI: Test Data-In. Data coming into the JTAG port.
 * - TDO: Test Data-Out. Data coming out of the JTAG port.
 * - TRST: Test Reset. Optional reset pin.
 *
 * Module Description
 * Very simple JTAG TAP meant to run two different test patterns
 * on an SoC module. Also integrated is a shift register that
 * will shift the output to the TDO pin.
 *
 * Module port description:
 * TCK, TDI, TRST, TDO
 * 	Standard JTAG ports.
 * TMS
 * 	Used to load data into shift register, which will get shifted out
 * socOutput
 * 	Output of SoC that feeds into shift register and gets shifted
 * 	out to TDO pin.
 * socCLK
 * 	Clock signal that goes to SoC module.
 * socRST
 * 	Reset signal that goes to SoC module.
 * socTestSel
 * 	Signal that goes to wrapper that selects which test condition
 * 	to do.
 */

module jtag_tap #(parameter WIDTH = 32) (TCK, TMS, TDI, TDO, TRST, socCLK, socRST, socOutput, socTestSel);

	/* Inputs */
	input TCK, TMS, TDI, TRST;
	input [WIDTH-1:0] socOutput;

	/* Outputs */
	output TDO, socCLK, socRST, socTestSel;

/* Signal assignments from JTAG interface to SoC module */
assign socCLK = TCK;
assign socRST = TRST;
assign socTestSel = TDI;

/* Shift register instantiation */
shift_register #(.LENGTH(WIDTH)) JTAG_OUT_SHFT_REG (.clk(TCK), .rst(TRST), .load(TMS), .socOutput(socOutput), .jtagOutput(TDO));

endmodule
