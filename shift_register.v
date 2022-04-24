/*
 * Shift Register
 * Simple shift register design that takes a 32-bit input
 * and shifts it to a single output
 */

module shift_register #(parameter LENGTH = 32) (clk, rst, socOutput, load, jtagOutput);

	input clk, rst, load;
	input [LENGTH-1:0] socOutput;

	output jtagOutput;

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
	/* If no reset or load then shift conents */
	else
		socData <= socData >> 1;

end

/* Concurrent statement assigning output */
assign jtagOutput = socData[0];

endmodule
