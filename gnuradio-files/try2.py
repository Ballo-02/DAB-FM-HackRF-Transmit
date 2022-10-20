#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# GNU Radio version: 3.10.4.0

from packaging.version import Version as StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from gnuradio import analog
from gnuradio import blocks
import pmt
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio.qtgui import Range, GrRangeWidget
from PyQt5 import QtCore
import osmosdr
import time



from gnuradio import qtgui

class try2(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "try2")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 256000
        self.rf_samp_rate = rf_samp_rate = 10240000
        self.rf_gain = rf_gain = 0
        self.quad_rate = quad_rate = 256000
        self.if_samp_rate = if_samp_rate = 1024000
        self.if_gain = if_gain = 1
        self.freq_2 = freq_2 = 94.4e6
        self.freq_1 = freq_1 = 93.4e6
        self.center_freq = center_freq = 93400000

        ##################################################
        # Blocks
        ##################################################
        self._rf_gain_range = Range(0, 50, 1, 0, 200)
        self._rf_gain_win = GrRangeWidget(self._rf_gain_range, self.set_rf_gain, "rf gain", "counter_slider", float, QtCore.Qt.Horizontal, "value")

        self.top_layout.addWidget(self._rf_gain_win)
        self._if_gain_range = Range(0, 50, 1, 1, 200)
        self._if_gain_win = GrRangeWidget(self._if_gain_range, self.set_if_gain, "if_gain", "counter_slider", float, QtCore.Qt.Horizontal, "value")

        self.top_layout.addWidget(self._if_gain_win)
        self._center_freq_range = Range(87500000, 900000000, 50000, 93400000, 200)
        self._center_freq_win = GrRangeWidget(self._center_freq_range, self.set_center_freq, "Center frequency", "counter_slider", float, QtCore.Qt.Horizontal, "value")

        self.top_layout.addWidget(self._center_freq_win)
        self.rational_resampler_xxx_3_0 = filter.rational_resampler_fff(
                interpolation=8,
                decimation=1,
                taps=[],
                fractional_bw=0)
        self.rational_resampler_xxx_2_0 = filter.rational_resampler_ccc(
                interpolation=10,
                decimation=1,
                taps=[],
                fractional_bw=0)
        self.osmosdr_sink_0_0 = osmosdr.sink(
            args="numchan=" + str(1) + " " + 'hackrf=0000000000000000874461dc2c53b057'
        )
        self.osmosdr_sink_0_0.set_sample_rate(rf_samp_rate)
        self.osmosdr_sink_0_0.set_center_freq(center_freq, 0)
        self.osmosdr_sink_0_0.set_freq_corr(0, 0)
        self.osmosdr_sink_0_0.set_gain(rf_gain, 0)
        self.osmosdr_sink_0_0.set_if_gain(if_gain, 0)
        self.osmosdr_sink_0_0.set_bb_gain(20, 0)
        self.osmosdr_sink_0_0.set_antenna('', 0)
        self.osmosdr_sink_0_0.set_bandwidth(0, 0)
        self.blocks_short_to_float_0_0 = blocks.short_to_float(1, 1)
        self.blocks_multiply_const_vxx_2_0 = blocks.multiply_const_cc(32768)
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_ff(0.000030)
        self.blocks_file_source_0_0 = blocks.file_source(gr.sizeof_short*1, '/home/owen/Documents/radio/DAB-FM-HackRF-Transmit/linux/src/stream2.fifo', True, 0, 0)
        self.blocks_file_source_0_0.set_begin_tag(pmt.PMT_NIL)
        self.analog_wfm_tx_0_0 = analog.wfm_tx(
        	audio_rate=samp_rate,
        	quad_rate=quad_rate,
        	tau=(75e-6),
        	max_dev=75e3,
        	fh=(-1.0),
        )


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_wfm_tx_0_0, 0), (self.rational_resampler_xxx_2_0, 0))
        self.connect((self.blocks_file_source_0_0, 0), (self.blocks_short_to_float_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.rational_resampler_xxx_3_0, 0))
        self.connect((self.blocks_multiply_const_vxx_2_0, 0), (self.osmosdr_sink_0_0, 0))
        self.connect((self.blocks_short_to_float_0_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.rational_resampler_xxx_2_0, 0), (self.blocks_multiply_const_vxx_2_0, 0))
        self.connect((self.rational_resampler_xxx_3_0, 0), (self.analog_wfm_tx_0_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "try2")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

    def get_rf_samp_rate(self):
        return self.rf_samp_rate

    def set_rf_samp_rate(self, rf_samp_rate):
        self.rf_samp_rate = rf_samp_rate
        self.osmosdr_sink_0_0.set_sample_rate(self.rf_samp_rate)

    def get_rf_gain(self):
        return self.rf_gain

    def set_rf_gain(self, rf_gain):
        self.rf_gain = rf_gain
        self.osmosdr_sink_0_0.set_gain(self.rf_gain, 0)

    def get_quad_rate(self):
        return self.quad_rate

    def set_quad_rate(self, quad_rate):
        self.quad_rate = quad_rate

    def get_if_samp_rate(self):
        return self.if_samp_rate

    def set_if_samp_rate(self, if_samp_rate):
        self.if_samp_rate = if_samp_rate

    def get_if_gain(self):
        return self.if_gain

    def set_if_gain(self, if_gain):
        self.if_gain = if_gain
        self.osmosdr_sink_0_0.set_if_gain(self.if_gain, 0)

    def get_freq_2(self):
        return self.freq_2

    def set_freq_2(self, freq_2):
        self.freq_2 = freq_2

    def get_freq_1(self):
        return self.freq_1

    def set_freq_1(self, freq_1):
        self.freq_1 = freq_1

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq
        self.osmosdr_sink_0_0.set_center_freq(self.center_freq, 0)




def main(top_block_cls=try2, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
