///////////////////////////////////////////////////////////////////////////
// C++ code generated with wxFormBuilder (version Dec 21 2009)
// http://www.wxformbuilder.org/
//
// PLEASE DO "NOT" EDIT THIS FILE!
///////////////////////////////////////////////////////////////////////////

#include "noname.h"

///////////////////////////////////////////////////////////////////////////

MyFrame1::MyFrame1( wxWindow* parent, wxWindowID id, const wxString& title, const wxPoint& pos, const wxSize& size, long style ) : wxFrame( parent, id, title, pos, size, style )
{
	this->SetSizeHints( wxDefaultSize, wxDefaultSize );
	
	the_statusbar = this->CreateStatusBar( 1, wxST_SIZEGRIP, wxID_ANY );
	the_menubar = new wxMenuBar( 0 );
	file_menu = new wxMenu();
	the_menubar->Append( file_menu, wxT("File") );
	
	edit_menu = new wxMenu();
	the_menubar->Append( edit_menu, wxT("Edit") );
	
	help_menu = new wxMenu();
	wxMenuItem* m_menuItem1;
	m_menuItem1 = new wxMenuItem( help_menu, wxID_ANY, wxString( wxT("About") ) , wxEmptyString, wxITEM_NORMAL );
	help_menu->Append( m_menuItem1 );
	
	the_menubar->Append( help_menu, wxT("Help") );
	
	this->SetMenuBar( the_menubar );
	
	wxBoxSizer* main_sizer;
	main_sizer = new wxBoxSizer( wxVERTICAL );
	
	the_notebook = new wxNotebook( this, wxID_ANY, wxDefaultPosition, wxDefaultSize, 0 );
	articles_tab = new wxPanel( the_notebook, wxID_ANY, wxDefaultPosition, wxDefaultSize, wxTAB_TRAVERSAL );
	wxBoxSizer* article_tab_sizer;
	article_tab_sizer = new wxBoxSizer( wxVERTICAL );
	
	keyword_static = new wxStaticText( articles_tab, wxID_ANY, wxT("Enter Keyword:"), wxDefaultPosition, wxDefaultSize, 0 );
	keyword_static->Wrap( -1 );
	keyword_static->SetFont( wxFont( wxNORMAL_FONT->GetPointSize(), 70, 90, 92, false, wxEmptyString ) );
	
	article_tab_sizer->Add( keyword_static, 0, wxLEFT|wxRIGHT|wxTOP, 10 );
	
	wxBoxSizer* keyword_sizer;
	keyword_sizer = new wxBoxSizer( wxHORIZONTAL );
	
	keyword_text = new wxTextCtrl( articles_tab, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	keyword_sizer->Add( keyword_text, 1, wxLEFT|wxRIGHT|wxTOP, 5 );
	
	go_button = new wxButton( articles_tab, wxID_ANY, wxT("Go!"), wxDefaultPosition, wxDefaultSize, 0 );
	keyword_sizer->Add( go_button, 0, wxLEFT|wxRIGHT|wxTOP, 5 );
	
	
	keyword_sizer->Add( 0, 0, 1, wxEXPAND, 5 );
	
	article_tab_sizer->Add( keyword_sizer, 0, wxEXPAND|wxLEFT, 5 );
	
	find_text = new wxStaticText( articles_tab, wxID_ANY, wxT("Search For:"), wxDefaultPosition, wxDefaultSize, 0 );
	find_text->Wrap( -1 );
	find_text->SetFont( wxFont( wxNORMAL_FONT->GetPointSize(), 70, 90, 92, false, wxEmptyString ) );
	
	article_tab_sizer->Add( find_text, 0, wxLEFT|wxRIGHT|wxTOP, 10 );
	
	wxBoxSizer* bSizer211;
	bSizer211 = new wxBoxSizer( wxHORIZONTAL );
	
	article_tab_sizer->Add( bSizer211, 1, wxEXPAND, 5 );
	
	wxString m_choice1Choices[] = { wxT("Articles"), wxT("Answers"), wxT("Microposts(Twitter)"), wxT("Wikis") };
	int m_choice1NChoices = sizeof( m_choice1Choices ) / sizeof( wxString );
	m_choice1 = new wxChoice( articles_tab, wxID_ANY, wxDefaultPosition, wxDefaultSize, m_choice1NChoices, m_choice1Choices, 0 );
	m_choice1->SetSelection( 0 );
	article_tab_sizer->Add( m_choice1, 0, wxLEFT|wxRIGHT, 10 );
	
	wxBoxSizer* bSizer20;
	bSizer20 = new wxBoxSizer( wxHORIZONTAL );
	
	results_static = new wxStaticText( articles_tab, wxID_ANY, wxT("Results:"), wxDefaultPosition, wxDefaultSize, 0 );
	results_static->Wrap( -1 );
	results_static->SetFont( wxFont( wxNORMAL_FONT->GetPointSize(), 70, 90, 92, false, wxEmptyString ) );
	
	bSizer20->Add( results_static, 1, wxALL|wxEXPAND, 10 );
	
	
	bSizer20->Add( 0, 0, 3, wxEXPAND, 5 );
	
	m_staticText14 = new wxStaticText( articles_tab, wxID_ANY, wxT("Add Note:"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText14->Wrap( -1 );
	m_staticText14->SetFont( wxFont( wxNORMAL_FONT->GetPointSize(), 70, 90, 92, false, wxEmptyString ) );
	
	bSizer20->Add( m_staticText14, 2, wxLEFT|wxRIGHT|wxTOP, 10 );
	
	article_tab_sizer->Add( bSizer20, 0, wxEXPAND, 5 );
	
	wxBoxSizer* bSizer9;
	bSizer9 = new wxBoxSizer( wxHORIZONTAL );
	
	results_text = new wxTextCtrl( articles_tab, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, wxTE_MULTILINE );
	bSizer9->Add( results_text, 6, wxBOTTOM|wxEXPAND|wxLEFT|wxRIGHT, 10 );
	
	m_textCtrl14 = new wxTextCtrl( articles_tab, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, wxTE_MULTILINE );
	bSizer9->Add( m_textCtrl14, 3, wxBOTTOM|wxEXPAND|wxLEFT|wxRIGHT, 10 );
	
	article_tab_sizer->Add( bSizer9, 18, wxBOTTOM|wxEXPAND|wxLEFT|wxRIGHT|wxTOP, 5 );
	
	wxBoxSizer* bSizer21;
	bSizer21 = new wxBoxSizer( wxHORIZONTAL );
	
	
	bSizer21->Add( 0, 0, 1, wxEXPAND, 5 );
	
	m_button7 = new wxButton( articles_tab, wxID_ANY, wxT("Add"), wxDefaultPosition, wxDefaultSize, 0 );
	bSizer21->Add( m_button7, 0, wxRIGHT, 9 );
	
	article_tab_sizer->Add( bSizer21, 3, wxEXPAND|wxLEFT|wxRIGHT, 5 );
	
	
	article_tab_sizer->Add( 0, 0, 1, wxEXPAND, 5 );
	
	articles_tab->SetSizer( article_tab_sizer );
	articles_tab->Layout();
	article_tab_sizer->Fit( articles_tab );
	the_notebook->AddPage( articles_tab, wxT("Articles"), true );
	notes_tab = new wxPanel( the_notebook, wxID_ANY, wxDefaultPosition, wxDefaultSize, wxTAB_TRAVERSAL );
	wxBoxSizer* bSizer2;
	bSizer2 = new wxBoxSizer( wxVERTICAL );
	
	notes_static = new wxStaticText( notes_tab, wxID_ANY, wxT("Added Notes:"), wxDefaultPosition, wxDefaultSize, 0 );
	notes_static->Wrap( -1 );
	notes_static->SetFont( wxFont( wxNORMAL_FONT->GetPointSize(), 70, 90, 92, false, wxEmptyString ) );
	
	bSizer2->Add( notes_static, 0, wxALL, 10 );
	
	notes_text = new wxTextCtrl( notes_tab, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, wxTE_MULTILINE|wxTE_RICH2|wxTE_WORDWRAP );
	bSizer2->Add( notes_text, 4, wxALL|wxEXPAND, 5 );
	
	
	bSizer2->Add( 0, 0, 1, wxEXPAND, 5 );
	
	notes_tab->SetSizer( bSizer2 );
	notes_tab->Layout();
	bSizer2->Fit( notes_tab );
	the_notebook->AddPage( notes_tab, wxT("Notes"), false );
	
	main_sizer->Add( the_notebook, 1, wxEXPAND | wxALL, 5 );
	
	this->SetSizer( main_sizer );
	this->Layout();
	the_toolbar = this->CreateToolBar( wxTB_HORIZONTAL, wxID_ANY ); 
	the_toolbar->AddSeparator();
	the_toolbar->AddTool( wxID_ANY, wxT("tool"), wxBitmap( wxT("crystal_ pro/24x24/actions/save_all.png"), wxBITMAP_TYPE_ANY ), wxNullBitmap, wxITEM_NORMAL, wxEmptyString, wxT("Save All Notes") );
	the_toolbar->AddSeparator();
	the_toolbar->AddTool( wxID_ANY, wxT("tool"), wxBitmap( wxT("crystal_ pro/24x24/actions/exit.png"), wxBITMAP_TYPE_ANY ), wxNullBitmap, wxITEM_NORMAL, wxEmptyString, wxT("Exit") );
	the_toolbar->Realize();
	
	
	this->Centre( wxBOTH );
}

MyFrame1::~MyFrame1()
{
}
