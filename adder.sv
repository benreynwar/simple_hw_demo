module adder_example #(
    integer WIDTH = 1
  ) (
    input logic clk,
    input logic rst,
    input logic i_valid,
    input logic [WIDTH-1:0] i_data_a,
    input logic [WIDTH-1:0] i_data_b,
    output logic o_valid,
    output logic [WIDTH+1-1:0] o_data
  );

  always_ff @(posedge clk) begin
    o_valid <= i_valid;
    o_data <= (WIDTH+1)'(i_data_a) + (WIDTH+1)'(i_data_b);
    if (~rst) begin
      o_valid <= 1'b0;
    end
  end

endmodule

