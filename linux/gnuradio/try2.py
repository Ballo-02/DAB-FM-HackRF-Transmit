#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# GNU Radio version: 3.10.4.0

from gnuradio import analog
from gnuradio import blocks
import pmt
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import osmosdr
import time




class try2(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet", catch_exceptions=True)

        ##################################################
        # Variables
        ##################################################
        self.variable_0 = variable_0 = 0
        self.samp_rate = samp_rate = 256000
        self.rf_samp_rate = rf_samp_rate = 10240000
        self.quad_rate = quad_rate = 256000
        self.if_samp_rate = if_samp_rate = 1024000

        ##################################################
        # Blocks
        ##################################################
        self.rational_resampler_xxx_3 = filter.rational_resampler_fff(
                interpolation=8,
                decimation=1,
                taps=[],
                fractional_bw=0)
        self.rational_resampler_xxx_2 = filter.rational_resampler_ccc(
                interpolation=10,
                decimation=1,
                taps=[],
                fractional_bw=0)
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=4,
                decimation=1,
                taps=[],
                fractional_bw=0)
        self.osmosdr_sink_0 = osmosdr.sink(
            args="numchan=" + str(1) + " " + 'hackrf=0000000000000000874461dc25a38957'
        )
        self.osmosdr_sink_0.set_sample_rate(rf_samp_rate)
        self.osmosdr_sink_0.set_center_freq(93.4e6, 0)
        self.osmosdr_sink_0.set_freq_corr(0, 0)
        self.osmosdr_sink_0.set_gain(50, 0)
        self.osmosdr_sink_0.set_if_gain(0, 0)
        self.osmosdr_sink_0.set_bb_gain(20, 0)
        self.osmosdr_sink_0.set_antenna('', 0)
        self.osmosdr_sink_0.set_bandwidth(0, 0)
        self.blocks_short_to_float_0 = blocks.short_to_float(1, 1)
        self.blocks_multiply_const_vxx_2 = blocks.multiply_const_cc(32768)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff(0.000030)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_short*1, '/home/owen/Documents/fm/stream1.fifo', True, 0, 0)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.analog_wfm_tx_0 = analog.wfm_tx(
        	audio_rate=samp_rate,
        	quad_rate=quad_rate,
        	tau=(75e-6),
        	max_dev=75e3,
        	fh=(-1.0),
        )


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_wfm_tx_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_short_to_float_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.rational_resampler_xxx_3, 0))
        self.connect((self.blocks_multiply_const_vxx_2, 0), (self.osmosdr_sink_0, 0))
        self.connect((self.blocks_short_to_float_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.rational_resampler_xxx_2, 0))
        self.connect((self.rational_resampler_xxx_2, 0), (self.blocks_multiply_const_vxx_2, 0))
        self.connect((self.rational_resampler_xxx_3, 0), (self.analog_wfm_tx_0, 0))


    def get_variable_0(self):
        return self.variable_0

    def set_variable_0(self, variable_0):
        self.variable_0 = variable_0

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

    def get_rf_samp_rate(self):
        return self.rf_samp_rate

    def set_rf_samp_rate(self, rf_samp_rate):
        self.rf_samp_rate = rf_samp_rate
        self.osmosdr_sink_0.set_sample_rate(self.rf_samp_rate)

    def get_quad_rate(self):
        return self.quad_rate

    def set_quad_rate(self, quad_rate):
        self.quad_rate = quad_rate

    def get_if_samp_rate(self):
        return self.if_samp_rate

    def set_if_samp_rate(self, if_samp_rate):
        self.if_samp_rate = if_samp_rate




def main(top_block_cls=try2, options=None):
    tb = top_block_cls()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        sys.exit(0)

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    tb.start()

    try:
        input('Press Enter to quit: ')
    except EOFError:
        pass
    tb.stop()
    tb.wait()


if __name__ == '__main__':
    main()
