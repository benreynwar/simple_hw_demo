import os

from random import Random
import cocotb
from cocotb import triggers, clock
from cocotb_test.simulator import run


@cocotb.test
async def adder_test(dut):
    seed = 0
    rnd = Random(seed)
    cocotb.fork(clock.Clock(dut.clk, 1000).start())
    last_expected_data = None
    max_value = pow(2, dut.i_data_a.value.n_bits)-1
    for i in range(20):
        valid = rnd.randint(0, 1)
        data_a = rnd.randint(0, max_value)
        data_b = rnd.randint(0, max_value)
        dut.i_valid.value = valid
        dut.i_data_a.value = data_a
        dut.i_data_b.value = data_b
        if valid == 1:
            expected_data = data_a + data_b
        else:
            expected_data = None
        await triggers.ReadOnly()
        if last_expected_data is not None:
            assert last_expected_data == dut.o_data.value
        await triggers.RisingEdge(dut.clk)
        last_expected_data = expected_data


def test_adder():
    files = ['adder.sv']
    run(
        verilog_sources=files,
        toplevel='adder_example',
        module='test_adder',
    )


if __name__ == '__main__':
    os.environ['SIM'] = 'verilator'
    test_adder()
