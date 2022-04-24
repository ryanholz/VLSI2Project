/*
 * Shift Register
 * Simple shift register design that takes a 32-bit input
 * and shifts it to a single output
 *
 * Shift register port description:
 * clk, rst
 * 	Clock and reset signals. Self explanatory.
 * load
 * 	Signal used to load the shift register with new data.
 * socOutput
 * 	Output of the SoC that gets shifted out through the jtagOutput
 * 	signal.
 * jtagOutput
 * 	Output of the shift register that will get shifted out through
 * 	the TDO JTAG output pin.
 */

module shift_register #(parameter LENGTH = 32) (clk, rst, socOutput, load, jtagOutput);

	/* Inputs */
	input clk, rst, load;
	input [LENGTH-1:0] socOutput;

	/* Outputs */
	output jtagOutput;

/* Additional signal used for shifting */
reg [LENGTH-1:0] socData;

/* Always block to trigger at the positive edge of the clock */
always @(posedge clk)
begin

	/* Synchronous reset */
	if(rst == 1)
		socData <= 0;
	/* Load signal for when to load new data into shift register */
	else if(load == 1)
		socData <= socOutput;
	/* If no reset or load then shift contents of register*/
	else
		socData <= socData >> 1;

end

/* Concurrent statement assigning jtagOutput */
assign jtagOutput = socData[0];

endmodule
