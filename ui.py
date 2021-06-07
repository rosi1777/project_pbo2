# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class Login
###########################################################################

class Login ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 655,390 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.login = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Login", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.login.Wrap( -1 )

		self.login.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Montserrat SemiBold" ) )

		bSizer3.Add( self.login, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.username = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.username.Wrap( -1 )

		self.username.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Montserrat Medium" ) )

		fgSizer1.Add( self.username, 0, wx.ALL, 5 )

		self.usernameCtrl = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), 0 )
		fgSizer1.Add( self.usernameCtrl, 0, wx.ALL, 5 )

		self.password = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.password.Wrap( -1 )

		self.password.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Montserrat Medium" ) )

		fgSizer1.Add( self.password, 0, wx.ALL, 5 )

		self.passwordCtrl = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), 0 )
		fgSizer1.Add( self.passwordCtrl, 0, wx.ALL, 5 )

		self.loginBtn = wx.Button( self.m_panel2, wx.ID_ANY, u"Login", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.loginBtn, 0, wx.ALL, 5 )


		bSizer3.Add( fgSizer1, 1, wx.EXPAND, 5 )


		self.m_panel2.SetSizer( bSizer3 )
		self.m_panel2.Layout()
		bSizer3.Fit( self.m_panel2 )
		bSizer1.Add( self.m_panel2, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.loginBtn.Bind( wx.EVT_BUTTON, self.loginBtnOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def loginBtnOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class InsertKaryawan
###########################################################################

class InsertKaryawan ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Insert Data", pos = wx.DefaultPosition, size = wx.Size( 388,494 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		DialogInser = wx.FlexGridSizer( 0, 2, 0, 0 )
		DialogInser.SetFlexibleDirection( wx.BOTH )
		DialogInser.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.inpUsername = wx.StaticText( self, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.inpUsername.Wrap( -1 )

		DialogInser.Add( self.inpUsername, 0, wx.ALL, 5 )

		self.ctrlUsername = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		DialogInser.Add( self.ctrlUsername, 0, wx.ALL, 5 )

		self.inpPassword = wx.StaticText( self, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.inpPassword.Wrap( -1 )

		DialogInser.Add( self.inpPassword, 0, wx.ALL, 5 )

		self.ctrlPassword = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		DialogInser.Add( self.ctrlPassword, 0, wx.ALL, 5 )

		self.inpNama = wx.StaticText( self, wx.ID_ANY, u"Nama", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.inpNama.Wrap( -1 )

		DialogInser.Add( self.inpNama, 0, wx.ALL, 5 )

		self.ctrlNama = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		DialogInser.Add( self.ctrlNama, 0, wx.ALL, 5 )

		self.inpGender = wx.StaticText( self, wx.ID_ANY, u"Gender", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.inpGender.Wrap( -1 )

		DialogInser.Add( self.inpGender, 0, wx.ALL, 5 )

		self.ctrlGender = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		DialogInser.Add( self.ctrlGender, 0, wx.ALL, 5 )

		self.inpALamat = wx.StaticText( self, wx.ID_ANY, u"Alamat", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.inpALamat.Wrap( -1 )

		DialogInser.Add( self.inpALamat, 0, wx.ALL, 5 )

		self.ctrlAlamat = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		DialogInser.Add( self.ctrlAlamat, 0, wx.ALL, 5 )

		self.inpTelepon = wx.StaticText( self, wx.ID_ANY, u"Telepon", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.inpTelepon.Wrap( -1 )

		DialogInser.Add( self.inpTelepon, 0, wx.ALL, 5 )

		self.ctrlTelepon = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		DialogInser.Add( self.ctrlTelepon, 0, wx.ALL, 5 )

		self.inpTahun = wx.StaticText( self, wx.ID_ANY, u"Tanggal Masuk", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.inpTahun.Wrap( -1 )

		DialogInser.Add( self.inpTahun, 0, wx.ALL, 5 )

		self.ctrlTahunMasuk = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		DialogInser.Add( self.ctrlTahunMasuk, 0, wx.ALL, 5 )


		DialogInser.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.submit = wx.Button( self, wx.ID_ANY, u"submit", wx.DefaultPosition, wx.DefaultSize, 0 )
		DialogInser.Add( self.submit, 0, wx.ALL, 5 )


		self.SetSizer( DialogInser )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.submit.Bind( wx.EVT_BUTTON, self.submitOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def submitOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class InsertBarang
###########################################################################

class InsertBarang ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"InsertBarang", pos = wx.DefaultPosition, size = wx.Size( 291,301 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		DialogInser = wx.FlexGridSizer( 0, 2, 0, 0 )
		DialogInser.SetFlexibleDirection( wx.BOTH )
		DialogInser.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.inpNama = wx.StaticText( self, wx.ID_ANY, u"Nama", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.inpNama.Wrap( -1 )

		DialogInser.Add( self.inpNama, 0, wx.ALL, 5 )

		self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		DialogInser.Add( self.m_textCtrl3, 0, wx.ALL, 5 )

		self.inpJual = wx.StaticText( self, wx.ID_ANY, u"Harga Jual", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.inpJual.Wrap( -1 )

		DialogInser.Add( self.inpJual, 0, wx.ALL, 5 )

		self.m_textCtrl5 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		DialogInser.Add( self.m_textCtrl5, 0, wx.ALL, 5 )

		self.inpBeli = wx.StaticText( self, wx.ID_ANY, u"Harga Beli", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.inpBeli.Wrap( -1 )

		DialogInser.Add( self.inpBeli, 0, wx.ALL, 5 )

		self.m_textCtrl6 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		DialogInser.Add( self.m_textCtrl6, 0, wx.ALL, 5 )

		self.inpStok = wx.StaticText( self, wx.ID_ANY, u"Stok", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.inpStok.Wrap( -1 )

		DialogInser.Add( self.inpStok, 0, wx.ALL, 5 )

		self.m_textCtrl24 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		DialogInser.Add( self.m_textCtrl24, 0, wx.ALL, 5 )

		self.submit = wx.Button( self, wx.ID_ANY, u"submit", wx.DefaultPosition, wx.DefaultSize, 0 )
		DialogInser.Add( self.submit, 0, wx.ALL, 5 )


		self.SetSizer( DialogInser )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class PenjualanPesanan
###########################################################################

class PenjualanPesanan ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Penjualan dan Pemesanan", pos = wx.DefaultPosition, size = wx.Size( 596,381 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		DialogInser = wx.FlexGridSizer( 0, 4, 0, 0 )
		DialogInser.SetFlexibleDirection( wx.BOTH )
		DialogInser.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.inpNama = wx.StaticText( self, wx.ID_ANY, u"Nama", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.inpNama.Wrap( -1 )

		DialogInser.Add( self.inpNama, 0, wx.ALL, 5 )

		self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		DialogInser.Add( self.m_textCtrl3, 0, wx.ALL, 5 )


		DialogInser.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		DialogInser.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.inpAlamat = wx.StaticText( self, wx.ID_ANY, u"Alamat", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.inpAlamat.Wrap( -1 )

		DialogInser.Add( self.inpAlamat, 0, wx.ALL, 5 )

		self.m_textCtrl5 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		DialogInser.Add( self.m_textCtrl5, 0, wx.ALL, 5 )


		DialogInser.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		DialogInser.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.inpBarang = wx.StaticText( self, wx.ID_ANY, u"Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.inpBarang.Wrap( -1 )

		DialogInser.Add( self.inpBarang, 0, wx.ALL, 5 )

		self.m_textCtrl6 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		DialogInser.Add( self.m_textCtrl6, 0, wx.ALL, 5 )


		DialogInser.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		DialogInser.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.inpJuml = wx.StaticText( self, wx.ID_ANY, u"Jumlah", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.inpJuml.Wrap( -1 )

		DialogInser.Add( self.inpJuml, 0, wx.ALL, 5 )

		self.m_textCtrl24 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		DialogInser.Add( self.m_textCtrl24, 0, wx.ALL, 5 )


		DialogInser.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		DialogInser.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.inpTanggal = wx.StaticText( self, wx.ID_ANY, u"Tanggal Pesan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.inpTanggal.Wrap( -1 )

		DialogInser.Add( self.inpTanggal, 0, wx.ALL, 5 )

		self.m_textCtrl18 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		DialogInser.Add( self.m_textCtrl18, 0, wx.ALL, 5 )


		DialogInser.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		DialogInser.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.inpStatus = wx.StaticText( self, wx.ID_ANY, u"Status", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.inpStatus.Wrap( -1 )

		DialogInser.Add( self.inpStatus, 0, wx.ALL, 5 )

		self.m_textCtrl19 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		DialogInser.Add( self.m_textCtrl19, 0, wx.ALL, 5 )


		DialogInser.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		DialogInser.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		DialogInser.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.submit = wx.Button( self, wx.ID_ANY, u"submit", wx.DefaultPosition, wx.DefaultSize, 0 )
		DialogInser.Add( self.submit, 0, wx.ALL, 5 )


		self.SetSizer( DialogInser )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class OwnerFrame
###########################################################################

class OwnerFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 836,472 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		fgSizer63 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer63.SetFlexibleDirection( wx.BOTH )
		fgSizer63.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		fgSizer63.Add( ( 677, 0), 1, wx.EXPAND, 5 )

		self.logout = wx.Button( self, wx.ID_ANY, u"Logout", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer63.Add( self.logout, 0, wx.ALL, 5 )


		bSizer3.Add( fgSizer63, 1, wx.EXPAND, 5 )

		self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.infoAkun = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.Akun = wx.grid.Grid( self.infoAkun, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.Akun.CreateGrid( 1, 3 )
		self.Akun.EnableEditing( True )
		self.Akun.EnableGridLines( True )
		self.Akun.EnableDragGridSize( False )
		self.Akun.SetMargins( 0, 0 )

		# Columns
		self.Akun.EnableDragColMove( False )
		self.Akun.EnableDragColSize( True )
		self.Akun.SetColLabelSize( 30 )
		self.Akun.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.Akun.EnableDragRowSize( True )
		self.Akun.SetRowLabelSize( 80 )
		self.Akun.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.Akun.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		fgSizer2.Add( self.Akun, 0, wx.ALL, 5 )

		self.ubahAkun = wx.Button( self.infoAkun, wx.ID_ANY, u"Ubah Akun", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.ubahAkun, 0, wx.ALL, 5 )


		self.infoAkun.SetSizer( fgSizer2 )
		self.infoAkun.Layout()
		fgSizer2.Fit( self.infoAkun )
		self.m_notebook1.AddPage( self.infoAkun, u"Info Akun", False )
		self.dataBarang = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer3 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.Barang = wx.grid.Grid( self.dataBarang, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.Barang.CreateGrid( 5, 5 )
		self.Barang.EnableEditing( True )
		self.Barang.EnableGridLines( True )
		self.Barang.EnableDragGridSize( False )
		self.Barang.SetMargins( 0, 0 )

		# Columns
		self.Barang.EnableDragColMove( False )
		self.Barang.EnableDragColSize( True )
		self.Barang.SetColLabelSize( 30 )
		self.Barang.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.Barang.EnableDragRowSize( True )
		self.Barang.SetRowLabelSize( 80 )
		self.Barang.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.Barang.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		fgSizer3.Add( self.Barang, 0, wx.ALL, 5 )


		self.dataBarang.SetSizer( fgSizer3 )
		self.dataBarang.Layout()
		fgSizer3.Fit( self.dataBarang )
		self.m_notebook1.AddPage( self.dataBarang, u"Data Barang", False )
		self.dataPesanan = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer4 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.Pesanan = wx.grid.Grid( self.dataPesanan, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.Pesanan.CreateGrid( 1, 7 )
		self.Pesanan.EnableEditing( True )
		self.Pesanan.EnableGridLines( True )
		self.Pesanan.EnableDragGridSize( False )
		self.Pesanan.SetMargins( 0, 0 )

		# Columns
		self.Pesanan.EnableDragColMove( False )
		self.Pesanan.EnableDragColSize( True )
		self.Pesanan.SetColLabelSize( 30 )
		self.Pesanan.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.Pesanan.EnableDragRowSize( True )
		self.Pesanan.SetRowLabelSize( 80 )
		self.Pesanan.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.Pesanan.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		fgSizer4.Add( self.Pesanan, 0, wx.ALL, 5 )


		self.dataPesanan.SetSizer( fgSizer4 )
		self.dataPesanan.Layout()
		fgSizer4.Fit( self.dataPesanan )
		self.m_notebook1.AddPage( self.dataPesanan, u"Data Pesanan", False )
		self.dataPenjualan = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer5 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.Penjualan = wx.grid.Grid( self.dataPenjualan, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.Penjualan.CreateGrid( 1, 7 )
		self.Penjualan.EnableEditing( True )
		self.Penjualan.EnableGridLines( True )
		self.Penjualan.EnableDragGridSize( False )
		self.Penjualan.SetMargins( 0, 0 )

		# Columns
		self.Penjualan.EnableDragColMove( False )
		self.Penjualan.EnableDragColSize( True )
		self.Penjualan.SetColLabelSize( 30 )
		self.Penjualan.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.Penjualan.EnableDragRowSize( True )
		self.Penjualan.SetRowLabelSize( 80 )
		self.Penjualan.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.Penjualan.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		fgSizer5.Add( self.Penjualan, 0, wx.ALL, 5 )


		self.dataPenjualan.SetSizer( fgSizer5 )
		self.dataPenjualan.Layout()
		fgSizer5.Fit( self.dataPenjualan )
		self.m_notebook1.AddPage( self.dataPenjualan, u"Data Penjualan", False )
		self.dataKaryawan = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.Karyawan = wx.grid.Grid( self.dataKaryawan, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.Karyawan.CreateGrid( 5, 8 )
		self.Karyawan.EnableEditing( True )
		self.Karyawan.EnableGridLines( True )
		self.Karyawan.EnableDragGridSize( False )
		self.Karyawan.SetMargins( 0, 0 )

		# Columns
		self.Karyawan.EnableDragColMove( False )
		self.Karyawan.EnableDragColSize( True )
		self.Karyawan.SetColLabelSize( 30 )
		self.Karyawan.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.Karyawan.EnableDragRowSize( True )
		self.Karyawan.SetRowLabelSize( 80 )
		self.Karyawan.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.Karyawan.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer4.Add( self.Karyawan, 0, wx.ALL, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		fgSizer8 = wx.FlexGridSizer( 1, 3, 0, 0 )
		fgSizer8.SetFlexibleDirection( wx.BOTH )
		fgSizer8.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.AdEmpBtn = wx.Button( self.dataKaryawan, wx.ID_ANY, u"Tambah", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.AdEmpBtn, 0, wx.ALL, 5 )


		bSizer4.Add( fgSizer8, 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.dataKaryawan.SetSizer( bSizer4 )
		self.dataKaryawan.Layout()
		bSizer4.Fit( self.dataKaryawan )
		self.m_notebook1.AddPage( self.dataKaryawan, u"Data Karyawan", True )

		bSizer3.Add( self.m_notebook1, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer3 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.logout.Bind( wx.EVT_BUTTON, self.logoutBtn )
		self.ubahAkun.Bind( wx.EVT_BUTTON, self.UpdateAccount )
		self.AdEmpBtn.Bind( wx.EVT_BUTTON, self.AdEmpBtnOnButtonClick )
		self.Karyawan.Bind(wx.grid.EVT_GRID_SELECT_CELL,
                     self.tabelEmployeeOnGridCmdSelectCell)

	def __del__(self):
		pass

	def tabelEmployeeOnGridCmdSelectCell(self, event):
		event.Skip()


	# Virtual event handlers, overide them in your derived class
	def logoutBtn( self, event ):
		event.Skip()

	def UpdateAccount( self, event ):
		event.Skip()

	def AdEmpBtnOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class EmployeeFrame
###########################################################################

class EmployeeFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 889,550 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.m_notebook2 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.barang = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		self.m_grid8 = wx.grid.Grid( self.barang, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid8.CreateGrid( 7, 5 )
		self.m_grid8.EnableEditing( True )
		self.m_grid8.EnableGridLines( True )
		self.m_grid8.EnableDragGridSize( False )
		self.m_grid8.SetMargins( 0, 0 )

		# Columns
		self.m_grid8.EnableDragColMove( False )
		self.m_grid8.EnableDragColSize( True )
		self.m_grid8.SetColLabelSize( 30 )
		self.m_grid8.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid8.EnableDragRowSize( True )
		self.m_grid8.SetRowLabelSize( 80 )
		self.m_grid8.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid8.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer6.Add( self.m_grid8, 0, wx.ALL, 5 )

		fgSizer10 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer10.SetFlexibleDirection( wx.BOTH )
		fgSizer10.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_button6 = wx.Button( self.barang, wx.ID_ANY, u"Tambah", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer10.Add( self.m_button6, 0, wx.ALL, 5 )

		self.m_button7 = wx.Button( self.barang, wx.ID_ANY, u"Ubah", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer10.Add( self.m_button7, 0, wx.ALL, 5 )

		self.m_button8 = wx.Button( self.barang, wx.ID_ANY, u"Hapus", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer10.Add( self.m_button8, 0, wx.ALL, 5 )


		bSizer6.Add( fgSizer10, 1, wx.EXPAND, 5 )


		self.barang.SetSizer( bSizer6 )
		self.barang.Layout()
		bSizer6.Fit( self.barang )
		self.m_notebook2.AddPage( self.barang, u"Data Barang", True )
		self.pesanan = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer71 = wx.BoxSizer( wx.VERTICAL )

		self.m_grid71 = wx.grid.Grid( self.pesanan, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid71.CreateGrid( 1, 7 )
		self.m_grid71.EnableEditing( True )
		self.m_grid71.EnableGridLines( True )
		self.m_grid71.EnableDragGridSize( False )
		self.m_grid71.SetMargins( 0, 0 )

		# Columns
		self.m_grid71.EnableDragColMove( False )
		self.m_grid71.EnableDragColSize( True )
		self.m_grid71.SetColLabelSize( 30 )
		self.m_grid71.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid71.EnableDragRowSize( True )
		self.m_grid71.SetRowLabelSize( 80 )
		self.m_grid71.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid71.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer71.Add( self.m_grid71, 0, wx.ALL, 5 )

		fgSizer81 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer81.SetFlexibleDirection( wx.BOTH )
		fgSizer81.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_button91 = wx.Button( self.pesanan, wx.ID_ANY, u"Add", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer81.Add( self.m_button91, 0, wx.ALL, 5 )

		self.m_button101 = wx.Button( self.pesanan, wx.ID_ANY, u"Update", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer81.Add( self.m_button101, 0, wx.ALL, 5 )

		self.m_button111 = wx.Button( self.pesanan, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer81.Add( self.m_button111, 0, wx.ALL, 5 )


		bSizer71.Add( fgSizer81, 1, wx.EXPAND, 5 )


		self.pesanan.SetSizer( bSizer71 )
		self.pesanan.Layout()
		bSizer71.Fit( self.pesanan )
		self.m_notebook2.AddPage( self.pesanan, u"Data Pesanan", False )
		self.penjualan = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		self.m_grid7 = wx.grid.Grid( self.penjualan, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid7.CreateGrid( 1, 7 )
		self.m_grid7.EnableEditing( True )
		self.m_grid7.EnableGridLines( True )
		self.m_grid7.EnableDragGridSize( False )
		self.m_grid7.SetMargins( 0, 0 )

		# Columns
		self.m_grid7.EnableDragColMove( False )
		self.m_grid7.EnableDragColSize( True )
		self.m_grid7.SetColLabelSize( 30 )
		self.m_grid7.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid7.EnableDragRowSize( True )
		self.m_grid7.SetRowLabelSize( 80 )
		self.m_grid7.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid7.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer7.Add( self.m_grid7, 0, wx.ALL, 5 )

		fgSizer8 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer8.SetFlexibleDirection( wx.BOTH )
		fgSizer8.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_button9 = wx.Button( self.penjualan, wx.ID_ANY, u"Add", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.m_button9, 0, wx.ALL, 5 )

		self.m_button10 = wx.Button( self.penjualan, wx.ID_ANY, u"Update", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.m_button10, 0, wx.ALL, 5 )

		self.m_button11 = wx.Button( self.penjualan, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.m_button11, 0, wx.ALL, 5 )


		bSizer7.Add( fgSizer8, 1, wx.EXPAND, 5 )


		self.penjualan.SetSizer( bSizer7 )
		self.penjualan.Layout()
		bSizer7.Fit( self.penjualan )
		self.m_notebook2.AddPage( self.penjualan, u"Data Penjualan", False )

		bSizer5.Add( self.m_notebook2, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer5 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class UpdateOwner
###########################################################################

class UpdateOwner ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 420,282 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		fgSizer69 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer69.SetFlexibleDirection( wx.BOTH )
		fgSizer69.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.username = wx.StaticText( self, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.username.Wrap( -1 )

		fgSizer69.Add( self.username, 0, wx.ALL, 5 )

		self.usrCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer69.Add( self.usrCtrl, 0, wx.ALL, 5 )

		self.password = wx.StaticText( self, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.password.Wrap( -1 )

		fgSizer69.Add( self.password, 0, wx.ALL, 5 )

		self.pswCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer69.Add( self.pswCtrl, 0, wx.ALL, 5 )

		self.nama = wx.StaticText( self, wx.ID_ANY, u"Nama", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.nama.Wrap( -1 )

		fgSizer69.Add( self.nama, 0, wx.ALL, 5 )

		self.nameCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer69.Add( self.nameCtrl, 0, wx.ALL, 5 )


		fgSizer69.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.submit = wx.Button( self, wx.ID_ANY, u"Submit", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer69.Add( self.submit, 0, wx.ALL, 5 )


		self.SetSizer( fgSizer69 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.submit.Bind( wx.EVT_BUTTON, self.submitUpdateOwner )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def submitUpdateOwner( self, event ):
		event.Skip()


