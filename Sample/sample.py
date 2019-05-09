from flask import Flask
from flask import render_template
app = Flask(__name__)

benjamin=[
    [
{'proj': 'tactic_development',
'scope': 'Shot/Bunch01/ALN_SC_13_SH_012',
'type': '2d_roto',
'int_version': 'V0001',
'reviewer': 'prabumurugesan',
'notes': 'test notes',
'attachment': '//san/10_TEMP_FILES/PIPE/tactic_development/DB/PFXDB/Shot/Bunch01/ALN_SC_13_SH_012/annotations/ScriptingListenerVB.log'},

{'proj': 'tactic_development',
'scope': 'Shot/Bunch01/ALN_SC_13_SH_012',
'type': '2d_roto',
'int_version': 'V0001',
'reviewer': 'prabumurugesan',
'notes': 'test notes',
'attachment': '//san/10_TEMP_FILES/PIPE/tactic_development/DB/PFXDB/Shot/Bunch01/ALN_SC_13_SH_012/annotations/ScriptingListenerVB.log'},

{'proj': 'tactic_development', 
'scope': 'Shot/Bunch01/ALN_SC_13_SH_012', 
'type': '2d_roto',
'int_version': 'V0001',
'reviewer': 'prabumurugesan',
'notes': 'Test Video',
'attachment': '//NAS/PFX_PROJECTS/tactic_development/DB/PFXDB/Shot/Bunch01/ALN_SC_13_SH_012/2d_roto/V0001/benjamin/QT/MOV/ROT_aln_ALN_SC_13_SH_012_ROT_V0001.MOV'},

{'proj': 'tactic_development',
'scope': 'Shot/Bunch01/ALN_SC_13_SH_012',
'type': '2d_roto', 
'int_version': 'V0001', 
'reviewer': 'prabumurugesan',
'notes': 'Test Image',
'attachment': '//Nas/pfx_projects/tactic_development/DB/PFXDB/Shot/Bunch01/ALN_SC_13_SH_012/art_mattepaint/V0001/matheswaran/Input/MP_ghostbusters_marquee.jpg'},

{'proj': 'tactic_development',
'scope': 'Shot/Bunch01/ALN_SC_13_SH_012',
'type': '2d_roto',
'int_version': 'V0001',
'reviewer': 'prabumurugesan',
'notes': 'lorem ipsum\r\n',
'attachment': ''}],



['aln', 'miab', 'wal', 'ild', 'sa2', 'tactic_development'],


['ROT', '2D_ELEMENT', 'PAINT', 'MATTEPAINT', 'CONCEPT_ART', '2D_LAYOUT', 'SLAPCOMP', 'PRECOMP', 'COMP', '2D_TEST', 'MATCHMOVE', 'MODEL', 'HDRI', 'RIGGING', 'SHADING', 'LOOKDEV', '3D_TEST', 'LIGHTING', 'DYNAMICS', 'SHOTSCULPT',     '3D_ANIMATION', 'TEXTURING', 'PREVIZ', 'PIPE_TEST', 'PIPE_OUT', '3D_LAYOUT']]

@app.route('/')
def hello_world():
    return render_template("index.html") 