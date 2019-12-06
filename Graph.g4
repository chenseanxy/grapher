grammar Graph;

program : (statement SEMICO)*  EOF
	;
statement :  statOrigin | statScale
          |  statRot    | statFor
          |  statColor
   ;

statOrigin : ORIGIN IS L_BRACKET expr
      COMMA expr R_BRACKET
    ;
statScale : SCALE IS L_BRACKET expr
      COMMA expr R_BRACKET
    ;
statRot : ROT IS expr
    ;
statFor : FOR T1 FROM expr TO expr
      STEP expr DRAW L_BRACKET expr COMMA
      expr R_BRACKET
    ;
statColor : COLOR IS C=(RED|BLACK|YELLOW|GREEN|BLUE)    #BuiltinColor
    | COLOR IS L_BRACKET expr COMMA expr COMMA expr R_BRACKET   #CustomColor
    ;
expr :
         <assoc=right>   expr POWER expr    #PowerExpr
      |  op=(PLUS | MINUS)  expr            #UnaryExpr
      |  expr op=(MUL  | DIV)   expr        #MulDivExpr
      |  expr op=(PLUS | MINUS) expr        #PlusMinusExpr

      |  CONST_ID                           #Const
      |  T1                                 #VarT
      |  ID   L_BRACKET  expr  R_BRACKET    #FuncExpr
      |  L_BRACKET       expr  R_BRACKET    #NestedExpr
      ;
PLUS   :	'+'  ;
MINUS  :	'-'  ;
DIV    :	'/'  ;
MUL    :	'*'  ;
POWER  :	'**' ;
SEMICO   :	';' ;
L_BRACKET:	'(' ;
R_BRACKET:	')' ;
COMMA    :	',' ;

ID : SIN
    | COS
    | TAN
    | LN
    | EXP
    | SQRT
    ;

CONST_ID :
       Integer
    |  Real
    |  NamedConst
    ;
fragment NamedConst : 'pi' | 'PI' | 'e' | 'E' ;
fragment Digits : [0-9]+ ;
fragment Integer : Digits;
fragment Fraction :
      Digits? '.' Digits
   |  Digits  '.'
   ;
fragment Exponent :
     [eE] [+-]? Digits
    ;
fragment Real :
        Fraction Exponent?
    |   Digits   Exponent
    ;

SIN : S I N;
COS : C O S;
TAN : T A N;
LN : L N;
EXP : E X P;
SQRT : S Q R T;
ORIGIN: O R I G I N;
SCALE : S C A L E  ;
ROT   : R O T      ;
IS    : I S        ;
COLOR : C O L O R  ;
TO    : T O        ;
STEP  : S T E P    ;
DRAW  : D R A W    ;
FOR   : F O R      ;
FROM  : F R O M    ;
T1    : T          ;
RED : R E D;
BLACK : B L A C K;
YELLOW : Y E L L O W;
GREEN : G R E E N;
BLUE : B L U E;
fragment A : [aA] ;
fragment B : [bB] ;
fragment C : [cC] ;
fragment D : [dD] ;
fragment E : [eE] ;
fragment F : [fF] ;
fragment G : [gG] ;
fragment H : [hH] ;
fragment I : [iI] ;
fragment J : [jJ] ;
fragment K : [kK] ;
fragment L : [lL] ;
fragment M : [mM] ;
fragment N : [nN] ;
fragment O : [oO] ;
fragment P : [pP] ;
fragment Q : [qQ] ;
fragment R : [rR] ;
fragment S : [sS] ;
fragment T : [tT] ;
fragment U : [uU] ;
fragment V : [vV] ;
fragment W : [wW] ;
fragment X : [xX] ;
fragment Y : [yY] ;
fragment Z : [zZ] ;
WS  :  [ \t\f\r\n]+  -> skip  // skip all blank
    ;
COMMENT:
	(   '//' ~[\r\n]*
	|  '--' ~[\r\n]*
	|  '/*' .*? '*/'    /* '?' for non-greedy */
	)  -> skip
	;
ErrText : . ;
