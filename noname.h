///////////////////////////////////////////////////////////////////////////
// C++ code generated with wxFormBuilder (version Dec 21 2009)
// http://www.wxformbuilder.org/
//
// PLEASE DO "NOT" EDIT THIS FILE!
///////////////////////////////////////////////////////////////////////////

#ifndef __noname__
#define __noname__

#include <wx/statusbr.h>
#include <wx/gdicmn.h>
#include <wx/font.h>
#include <wx/colour.h>
#include <wx/settings.h>
#include <wx/string.h>
#include <wx/menu.h>
#include <wx/bitmap.h>
#include <wx/image.h>
#include <wx/icon.h>
#include <wx/stattext.h>
#include <wx/textctrl.h>
#include <wx/button.h>
#include <wx/sizer.h>
#include <wx/choice.h>
#include <wx/panel.h>
#include <wx/notebook.h>
#include <wx/toolbar.h>
#include <wx/frame.h>

///////////////////////////////////////////////////////////////////////////


///////////////////////////////////////////////////////////////////////////////
/// Class MyFrame1
///////////////////////////////////////////////////////////////////////////////
class MyFrame1 : public wxFrame 
{
	private:
	
	protected:
		wxStatusBar* the_statusbar;
		wxMenuBar* the_menubar;
		wxMenu* file_menu;
		wxMenu* edit_menu;
		wxMenu* help_menu;
		wxNotebook* the_notebook;
		wxPanel* articles_tab;
		wxStaticText* keyword_static;
		wxTextCtrl* keyword_text;
		wxButton* go_button;
		
		wxStaticText* find_text;
		wxChoice* m_choice1;
		wxStaticText* results_static;
		
		wxStaticText* m_staticText14;
		wxTextCtrl* results_text;
		wxTextCtrl* m_textCtrl14;
		
		wxButton* m_button7;
		
		wxPanel* notes_tab;
		wxStaticText* notes_static;
		wxTextCtrl* notes_text;
		
		wxToolBar* the_toolbar;
	
	public:
		
		MyFrame1( wxWindow* parent, wxWindowID id = wxID_ANY, const wxString& title = wxT("Research Assistant"), const wxPoint& pos = wxDefaultPosition, const wxSize& size = wxSize( 500,418 ), long style = wxDEFAULT_FRAME_STYLE|wxTAB_TRAVERSAL );
		~MyFrame1();
	
};

#endif //__noname__
