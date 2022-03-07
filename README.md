# LISTALIGN

is a tiny package for aligning two sequences of strings, that are tokenized differently in efficent manner. If you get some nasty tokenized strings and need to map them back to these nasty indices, this is a way.

```
seq_1 = 'Thequickbrownfoxjumpedoverthelazydog'.replace('o', 'o ').split(' ')
['Thequickbro', 'wnfo', 'xjumpedo', 'verthelazydo', 'g']

seq_2 = 'The quick brown fox jumped over the lazy dog'.replace('e', 'e ').split(' ')
['The', '', 'quick', 'brown', 'fox', 'jumpe', 'd', 'ove', 'r', 'the', '', 'lazy', 'dog']


>>> suffix_align(seq_1, seq_2)
[(0, 0), (0, 2), (0, 3), (1, 3), (1, 4), (2, 4), (2, 5), (2, 6), (2, 7), (3, 7), (3, 8), (3, 9), (3, 11), (3, 12), (4, 12)]

```

Or as a table:

```

i         w1         w2     i   j 
==================================
0     Thequickbro   The     0   0 
1     Thequickbro   quick   0   2 
2     Thequickbro   brown   0   3 
3            wnfo   brown   1   3 
4            wnfo   fox     1   4 
5        xjumpedo   fox     2   4 
6        xjumpedo   jumpe   2   5 
7        xjumpedo   d       2   6 
8        xjumpedo   ove     2   7 
9    verthelazydo   ove     3   7 
10   verthelazydo   r       3   8 
11   verthelazydo   the     3   9 
12   verthelazydo   lazy    3   11
13   verthelazydo   dog     3   12
14              g   dog     4   12
```

They have to sum up to the same string. So if your texts are in the same order and have the same characters, this can be your solution. If not remove the differing characters and get them in the same order. Difflib has some tools to make the strings similar. https://docs.python.org/3/library/difflib.html

It does - without the fuzzyness - something similar as https://pypi.org/project/paired/ avoiding the O^3 complexity and without some errors. On my machine it aligns 100000 words in 500ms. With paired you will need more and stick to  under 1000 words. The same example used above does not work well with paired:

```

i         w1         w2      i     j 
=====================================
0             xxx   The     None   0 
1             xxx           None   1 
2             xxx   quick   None   2 
3             xxx   brown   None   3 
4             xxx   fox     None   4 
5             xxx   jumpe   None   5 
6             xxx   d       None   6 
7             xxx   ove     None   7 
8     Thequickbro   r          0   8 
9            wnfo   the        1   9 
10       xjumpedo              2   10
11   verthelazydo   lazy       3   11
12              g   dog        4   12
```

The algorithm working is a custom suffix tree, that remembers position of both lists, that were fed in. It seems to have O(n)- time complexity. No actual string comparison is involved. 


![alt text](./suffix-align_pa.png "Logo Title Text 1")

![alt text](./suffix-align.png "Logo Title Text 1")

This is, because the alignment problem is not solved like a classical alignment problem, that is bound to O^2 to construct a matrix, but like iterating through both lists once at the same time. Even if it looks like an alignment problem, it's not necessarily one.

## Get it

```
pip install listalign
```

# Run it

```
suffix_align(seq_1, seq_2)
```

# What's next

* add some fuzzyness
* diff-like support, that detects shifts between the sequences
* add parallelisation abilities



```angular2html

 None),
 (1856, 1282),
 (1856, 1283),
 (1857, 1283),
 (1858, 1284),
 (1859, 1285),
 (1860, 1287),
 (1860, 1286),
 (1861, 1288),
 (1862, None),
 (1862, 1289),
 (1863, 1289),
 (1864, 1290),
 (1865, 1291),
 (1866, 1292),
 (1867, 1293),
 (1868, 1295),
 (1868, 1294),
 (1869, 1296),
 (1870, 1297),
 (1870, None),
 (1871, 1297),
 (1872, 1298),
 (1873, None),
 (1873, 1299),
 (1873, 1300),
 (1874, 1300),
 (1875, 1302),
 (1875, 1301),
 (1876, 1303),
 (1877, 1304)]
 i                w1                      w2             i      j  
===================================================================
 0                          ∅-1   High                  None   784 
 1                          ∅-1   b_tw__n               None   1278
 2                          ∅-1   s_ns_                 None   231 
 3                          ∅-1   foot                  None   905 
 4                          ∅-1   r_ady                 None   496 
 5                          ∅-1   through               None   123 
 6                          ∅-1   caus_                 None   653 
 7                          ∅-1   call                  None   630 
 8                          ∅-1   full                  None   221 
 9                          ∅-1   und_r                 None   1016
 10                         ∅-1   stud_nt.Drop          None   463 
 11                         ∅-1   v_ry                  None   993 
 12                         ∅-1   _xp_ct                None   620 
 13                         ∅-1   land                  None   970 
 14                         ∅-1   Chang_                None   741 
 15                         ∅-1   und_r                 None   332 
 16                         ∅-1   f_ar                  None   453 
 17                         ∅-1   Congr_ss.             None   718 
 18                         ∅-1   cultural.             None   574 
 19                         ∅-1   upon                  None   1248
 20                         ∅-1   its_lf                None   165 
 21                         ∅-1   wh_th_r               None   201 
 22                         ∅-1   imagin_               None   1104
 23                         ∅-1   voic_.                None   695 
 24                         ∅-1   m_dia                 None   57  
 25                         ∅-1   Both                  None   960 
 26                         ∅-1   amount                None   322 
 27                         ∅-1   if                    None   1225
 28                         ∅-1   stuff                 None   443 
 29                         ∅-1   sci_ntist             None   937 
 30                         ∅-1   d_mocratic            None   708 
 31                         ∅-1   hundr_d.              None   973 
 32                         ∅-1   sort.                 None   685 
 33                         ∅-1   part                  None   47  
 34                         ∅-1   alr_ady.              None   397 
 35                         ∅-1   thr_at                None   168 
 36                         ∅-1   th_n                  None   1071
 37                         ∅-1   station               None   662 
 38                         ∅-1   Cam_ra                None   410 
 39                         ∅-1   sinc_                 None   1   
 40                         ∅-1   truth                 None   675 
 41                         ∅-1   imag_                 None   796 
 42                         ∅-1   imagin_.              None   387 
 43                         ∅-1   aft_r.                None   243 
 44                         ∅-1   b_autiful             None   1182
 45                         ∅-1   hav_                  None   364 
 46                         ∅-1   pr_tty                None   256 
 47                         ∅-1   might.Military        None   750 
 48                         ∅-1   know.At               None   1280
 49                         ∅-1   Wat_r                 None   1051
 50                         ∅-1   Today                 None   907 
 51                         ∅-1   _ntir_                None   498 
 52                         ∅-1   soci_ty               None   1172
 53                         ∅-1   light                 None   102 
 54                         ∅-1   which                 None   861 
 55                         ∅-1   t_nd.                 None   632 
 56                         ∅-1   color                 None   488 
 57                         ∅-1   N_xt                  None   344 
 58                         ∅-1   caus_                 None   465 
 59                         ∅-1   data                  None   730 
 60                         ∅-1   Anyon_                None   357 
 61                         ∅-1   bag                   None   213 
 62                         ∅-1   Tax                   None   478 
 63                         ∅-1   fr__                  None   334 
 64                         ∅-1   Tr_at                 None   828 
 65                         ∅-1   Stop                  None   311 
 66                         ∅-1   public.               None   1214
 67                         ∅-1   Nor                   None   985 
 68                         ∅-1   m_ssag_.              None   288 
 69                         ∅-1   Staff                 None   445 
 70                         ∅-1   soci_ty               None   831 
 71                         ∅-1   hom_                  None   687 
 72                         ∅-1   citiz_n               None   134 
 73                         ∅-1   past                  None   399 
 74                         ∅-1   thought               None   520 
 75                         ∅-1   pull.Room             None   641 
 76                         ∅-1   child.R_m_mb_r        None   1027
 77                         ∅-1   r_spond               None   389 
 78                         ∅-1   south                 None   1148
 79                         ∅-1   y_s                   None   919 
 80                         ∅-1   s__                   None   137 
 81                         ∅-1   _y_                   None   896 
 82                         ∅-1   aft_r                 None   523 
 83                         ∅-1   rol_                  None   114 
 84                         ∅-1   room                  None   379 
 85                         ∅-1   church                None   1282
 86                         ∅-1   Prop_rty              None   873 
 87                         ∅-1   _nvironm_ntal         None   235 
 88                         ∅-1   _v_ning               None   1138
 89                         ∅-1   Op_n                  None   500 
 90                         ∅-1   Continu_              None   1259
 91                         ∅-1   mod_l                 None   248 
 92                         ∅-1   if.                   None   1151
 93                         ∅-1   Sh_                   None   1007
 94                         ∅-1   town.                 None   863 
 95                         ∅-1   p_r.                  None   225 
 96                         ∅-1   int_rnational         None   755 
 97                         ∅-1   administration        None   840 
 98                         ∅-1   prov_                 None   1141
 99                         ∅-1   activity.             None   300 
100                         ∅-1   lay                   None   565 
101                         ∅-1   Pr_sid_nt             None   601 
102                         ∅-1   Wh_th_r               None   192 
103                         ∅-1   simpl_                None   25  
104                         ∅-1   you                   None   820 
105                         ∅-1   R_main                None   1085
106                         ∅-1   Our                   None   38  
107                         ∅-1   Fiv_                  None   941 
108                         ∅-1   card                  None   303 
109                         ∅-1   H_ar                  None   1206
110                         ∅-1   d_cad_                None   568 
111                         ∅-1   form_r                None   159 
112                         ∅-1   Fast                  None   1062
113                         ∅-1   Stor_                 None   15  
114                         ∅-1   cours_                None   954 
115                         ∅-1   mom_nt                None   414 
116                         ∅-1   mod_l                 None   5   
117                         ∅-1   book                  None   764 
118                         ∅-1   n_c_ssary.Rul_        None   126 
119                         ∅-1   individual            None   800 
120                         ∅-1   r_ality               None   1294
121                         ∅-1   difficult             None   885 
122                         ∅-1   r_sponsibility        None   656 
123                         ∅-1   rang_                 None   921 
124                         ∅-1   pick                  None   1042
125                         ∅-1   citiz_n.              None   1019
126                         ∅-1   _xp_ct                None   610 
127                         ∅-1   dr_am                 None   502 
128                         ∅-1   Custom_r              None   996 
129                         ∅-1   s_at.                 None   767 
130                         ∅-1   mod_l.                None   623 
131                         ∅-1   sist_r                None   744 
132                         ∅-1   such                  None   1274
133                         ∅-1   song                  None   721 
134                         ∅-1   consid_r              None   492 
135                         ∅-1   story                 None   577 
136                         ∅-1   stand.Prot_ct         None   1107
137                         ∅-1   participant           None   878 
138                         ∅-1   B_li_v_               None   469 
139                         ∅-1   ord_r                 None   60  
140                         ∅-1   magazin_              None   181 
141                         ∅-1   situation.            None   544 
142                         ∅-1   n_c_ssary             None   1218
143                         ∅-1   n_c_ssary             None   171 
144                         ∅-1   r_sponsibility        None   845 
145                         ∅-1   cl_arly               None   930 
146                         ∅-1   million               None   1195
147                         ∅-1   r_fl_ct               None   1087
148                         ∅-1   fund.                 None   1208
149                         ∅-1   start                 None   17  
150                         ∅-1   writ_                 None   282 
151                         ∅-1   b_com_                None   776 
152                         ∅-1   summ_r.               None   789 
153                         ∅-1   R_duc_                None   151 
154                         ∅-1   final                 None   537 
155                         ∅-1   cl_arly.              None   887 
156                         ∅-1   fri_nd                None   779 
157                         ∅-1   gas                   None   1044
158                      ﬁSmile   ﬁSmil_                   0   0   
159                         ∅-1   qu_stion              None   1129
160                         ∅-1   ah_ad.                None   900 
161                         ∅-1   Smil_                 None   82  
162                         ∅-1   ability               None   1286
163                         ∅-1   Final                 None   239 
164                         ∅-1   Card                  None   733 
165                         ∅-1   about                 None   504 
166                         ∅-1   clos_.Siz_            None   589 
167                         ∅-1   apply                 None   1263
168                         ∅-1   voic_                 None   216 
169                         ∅-1   op_n                  None   72  
170                         ∅-1   m_dia                 None   337 
171                         ∅-1   Summ_r                None   49  
172                         ∅-1   succ_ssful            None   314 
173                         ∅-1   liv_                  None   700 
174                         ∅-1   structur_             None   62  
175                         ∅-1   ok                    None   965 
176                         ∅-1   Congr_ss              None   857 
177                         ∅-1   both                  None   448 
178                         ∅-1   call                  None   1243
179                         ∅-1   stud_nt               None   690 
180                         ∅-1   y_t                   None   317 
181                         ∅-1   Ch_ck                 None   811 
182                         ∅-1   if                    None   1076
183                         ∅-1   mission.              None   667 
184                         ∅-1   growth.Yours_lf       None   271 
185                         ∅-1   clos_                 None   42  
186                         ∅-1   Allow                 None   1174
187                         ∅-1   n_ws                  None   513 
188                         ∅-1   Us_                   None   140 
189                         ∅-1   curr_nt               None   261 
190                         ∅-1   _ach                  None   1164
191                         ∅-1   _nvironm_nt           None   94  
192                         ∅-1   candidat_             None   480 
193                         ∅-1   spring                None   1154
194                         ∅-1   option                None   1010
195                         ∅-1   national              None   84  
196                         ∅-1   c_rtainly             None   1252
197                         ∅-1   r_s_arch              None   1023
198                         ∅-1   stor_                 None   205 
199                         ∅-1   Voic_                 None   97  
200                         ∅-1   Pric_                 None   1000
201                         ∅-1   bank.                 None   627 
202                         ∅-1   positiv_.             None   218 
203                         ∅-1   any                   None   1121
204                         ∅-1   a.Morning             None   712 
205                         ∅-1   _ffort                None   1098
206                         ∅-1   plan                  None   990 
207                         ∅-1   chair                 None   581 
208                         ∅-1   r_lat_                None   437 
209                         ∅-1   cultural              None   1111
210                         ∅-1   fact.Incr_as_         None   823 
211                         ∅-1   w_ll                  None   594 
212                         ∅-1   off                   None   185 
213                         ∅-1   body                  None   836 
214                         ∅-1   how_v_r               None   548 
215                         ∅-1   _y_.Th_ms_lv_s        None   1222
216                         ∅-1   miss.                 None   404 
217                         ∅-1   drop.                 None   440 
218                         ∅-1   Sp_cific              None   1055
219                         ∅-1   and                   None   417 
220                         ∅-1   d_spit_               None   911 
221                         ∅-1   Agr__                 None   394 
222                         ∅-1   should_r              None   1068
223                         ∅-1   s_v_ral               None   924 
224                         ∅-1   par_nt                None   515 
225                         ∅-1   star.                 None   371 
226                         ∅-1   b_st                  None   407 
227                         ∅-1   would                 None   672 
228                         ∅-1   Top                   None   757 
229                         ∅-1   h_                    None   528 
230                         ∅-1   buy.Forg_t            None   1143
231                         ∅-1   anything              None   914 
232                         ∅-1   Standard              None   1179
233                         ∅-1   dark                  None   891 
234                         ∅-1   stat_                 None   747 
235                         ∅-1   fish                  None   109 
236                         ∅-1   Who                   None   724 
237                         ∅-1   thought.              None   351 
238                         ∅-1   moth_r                None   616 
239                         ∅-1   my                    None   472 
240                         ∅-1   n_ar                  None   1002
241                         ∅-1   follow.               None   485 
242                         ∅-1   r_st                  None   341 
243                         ∅-1   oth_r.                None   606 
244                         ∅-1   official.Loss         None   197 
245                         ∅-1   stuff                 None   462 
246                         ∅-1   sur_                  None   53  
247                         ∅-1   En_rgy                None   583 
248                         ∅-1   sourc_                None   1257
249                         ∅-1   For_ign               None   1113
250                         ∅-1   list_n.               None   30  
251                         ∅-1   wind                  None   946 
252                         ∅-1   b_for_.               None   429 
253                         ∅-1   and.                  None   20  
254                         ∅-1   Talk                  None   285 
255                         ∅-1   voic_                 None   1188
256                         ∅-1   church.               None   1080
257                         ∅-1   l_ast                 None   792 
258                         ∅-1   attack.               None   563 
259                         ∅-1   this                  None   1057
260                         ∅-1   D__p                  None   648 
261                         ∅-1   coll_ction            None   419 
262                         ∅-1   _nt_r                 None   131 
263                         ∅-1   singl_                None   805 
264                         ∅-1   v_ry                  None   1299
265                         ∅-1   _ff_ct                None   517 
266                         ∅-1   m_ntion               None   1191
267                         ∅-1   Id_ntify              None   638 
268                         ∅-1   d__p                  None   265 
269                         ∅-1   across                None   1168
270                         ∅-1   incr_as_              None   880 
271                         ∅-1   _v_rybody             None   1145
272                         ∅-1   Fall                  None   916 
273                         ∅-1   oth_rs                None   507 
274                         ∅-1   t_nd                  None   1037
275                         ∅-1   finish.               None   75  
276                         ∅-1   air.                  None   111 
277                         ∅-1   th_m                  None   376 
278                         ∅-1   Sugg_st               None   870 
279                         ∅-1   Scor_                 None   762 
280                         ∅-1   f__l                  None   353 
281                         ∅-1   forg_t                None   847 
282                         ∅-1   gun.                  None   618 
283                         ∅-1   two                   None   209 
284                         ∅-1   d_spit_               None   330 
285                         ∅-1   charg_                None   1233
286                         ∅-1   th_r_                 None   1004
287                         ∅-1   plant.                None   1269
288                         ∅-1   hand                  None   1125
289                         ∅-1   coll_g_               None   307 
290                         ∅-1   l_tt_r                None   693 
291                         ∅-1   L_ast                 None   176 
292                         ∅-1   B_n_fit               None   850 
293                         ∅-1   history.              None   706 
294                         ∅-1   Ago                   None   297 
295                         ∅-1   study.                None   1200
296                         ∅-1   _njoy                 None   1236
297                         ∅-1   n_ws                  None   153 
298                         ∅-1   y_s                   None   1092
299                         ∅-1   cr_at_                None   274 
300                         ∅-1   word                  None   431 
301                         ∅-1   Ev_ryon_              None   552 
302                         ∅-1   tru_                  None   1046
303                         ∅-1   popular               None   817 
304                         ∅-1   r_sponsibility        None   1082
305                         ∅-1   w_ll.                 None   120 
306                         ∅-1   call.                 None   421 
307                         ∅-1   finish                None   771 
308                         ∅-1   act                   None   807 
309                         ∅-1   r_m_mb_r              None   1301
310                         ∅-1   f_w.                  None   1157
311                   sincewh?m   sinc_                    1   1   
312                   sincewh?m   whom                     1   2   
313                      event.           ∅-2              2   None
314                      event.   _v_nt.                   2   3   
315                               _v_nt.                   3   3   
316                         Bar   Bar                      4   4   
317                m?delcurrent   curr_nt                  5   6   
318                m?delcurrent   mod_l                    5   5   
319                       full.           ∅-2              6   None
320                       full.   full.                    6   7   
321                               full.                    7   7   
322                      Wind?w   Window                   8   8   
323                        like   lik_                     9   9   
324                     machine   machin_                 10   10  
325                    training   training                11   11  
326                  dem?cratic   d_mocratic              12   12  
327                     several   s_v_ral                 13   13  
328                    secti?n.   s_ction.                14   14  
329                  St?replant   plant                   15   16  
330                  St?replant   Stor_                   15   15  
331                  St?replant           ∅-2             15   None
332                               plant                   16   16  
333                   startthus   start                   17   17  
334                   startthus   thus                    17   18  
335                     message   m_ssag_                 18   19  
336                     message           ∅-2             18   None
337                               m_ssag_                 19   19  
338                    and.Feel   F__l                    20   21  
339                    and.Feel   and.                    20   20  
340                     c?mpany   company                 21   22  
341                      simply   simply                  22   23  
342                alm?st.Adult   almost.Adult            23   24  
343                alm?st.Adult           ∅-2             23   None
344                               almost.Adult            24   24  
345                simpleplayer   play_r                  25   26  
346                simpleplayer   simpl_                  25   25  
347                                       ∅-2             26   None
348                    electi?n   _l_ction                27   27  
349                     defense   d_f_ns_                 28   28  
350                       th?se   thos_                   29   29  
351                 listen.Thus           ∅-2             30   None
352                 listen.Thus   list_n.                 30   30  
353                 listen.Thus   Thus                    30   31  
354                               Thus                    31   31  
355                       happy   happy                   32   32  
356                       first   first                   33   33  
357                       share   shar_                   34   34  
358                       t?day   today                   35   35  
359                     capital   capital                 36   36  
360                        bad.   bad.                    37   37  
361                 Ourmarriage   Our                     38   38  
362                 Ourmarriage           ∅-2             38   None
363                 Ourmarriage   marriag_                38   39  
364                               marriag_                39   39  
365                  character.   charact_r.              40   40  
366                     Inv?lve   Involv_                 41   41  
367          cl?seair.Newspaper   clos_                   42   42  
368          cl?seair.Newspaper   air.N_wspap_r           42   43  
369                       speak   sp_ak                   43   44  
370                         see   s__                     44   45  
371                      animal   animal                  45   46  
372                      animal           ∅-2             45   None
373                               animal                  46   46  
374                 partnumber.   part                    47   47  
375                 partnumber.   numb_r.                 47   48  
376                 partnumber.           ∅-2             47   None
377                               numb_r.                 48   48  
378                  Summerreal   r_al                    49   50  
379                  Summerreal   Summ_r                  49   49  
380                   attenti?n   att_ntion               50   51  
381                     f?rward           ∅-2             51   None
382                     f?rward   forward                 51   52  
383                               forward                 52   52  
384              sureincluding.           ∅-2             53   None
385              sureincluding.   sur_                    53   53  
386              sureincluding.   including.              53   54  
387                               including.              54   54  
388                  Officialus   us                      55   56  
389                  Officialus   Official                55   55  
390                               us                      56   56  
391                  mediah?pe.   hop_.                   57   58  
392                  mediah?pe.   m_dia                   57   57  
393                        Case   Cas_                    58   59  
394                        Case           ∅-2             58   None
395                               Cas_                    59   59  
396                 ?rdernati?n   ord_r                   60   60  
397                 ?rdernati?n   nation                  60   61  
398                 ?rdernati?n           ∅-2             60   None
399                               nation                  61   61  
400              structurethank   thank                   62   63  
401              structurethank   structur_               62   62  
402                    ability.           ∅-2             63   None
403                    ability.   ability.                63   64  
404                               ability.                64   64  
405                         Ask   Ask                     65   65  
406                   c?nditi?n   condition               66   66  
407                          my   my                      67   67  
408            sure.Clearlyelse   sur_.Cl_arly            68   68  
409            sure.Clearlyelse   _ls_                    68   69  
410                               _ls_                    69   69  
411                         car   car                     70   70  
412                       civil   civil                   71   71  
413                ?penpressure   pr_ssur_                72   73  
414                ?penpressure           ∅-2             72   None
415                ?penpressure   op_n                    72   72  
416                               pr_ssur_                73   73  
417                      career   car__r                  74   74  
418                finish.Great   finish.                 75   75  
419                finish.Great   Gr_at                   75   76  
420                        c?st   cost                    76   77  
421                         win   win                     77   78  
422                         win           ∅-2             77   None
423                               win                     78   78  
424                    Dem?crat   D_mocrat                79   79  
425                     yet?ur.   y_t                     80   80  
426                     yet?ur.   our.                    80   81  
427                               our.                    81   81  
428                   Smilefull   full                    82   83  
429                   Smilefull           ∅-2             82   None
430                   Smilefull   Smil_                   82   82  
431                               full                    83   83  
432           nati?nalsh?ulder.   national                84   84  
433           nati?nalsh?ulder.   should_r.               84   85  
434                      Auth?r   Author                  85   86  
435                      Auth?r           ∅-2             85   None
436                               Author                  86   86  
437                  c?mmercial   comm_rcial              87   87  
438                      eff?rt   _ffort                  88   88  
439                   p?ssible.   possibl_.               89   89  
440                    Resp?nse   R_spons_                90   90  
441                    research   r_s_arch                91   91  
442                        away   away                    92   92  
443          j?in.T?ughh?spital   join.N_twork            93   93  
444          j?in.T?ughh?spital           ∅-2             93   None
445                    American           ∅-2             94   None
446                                       ∅-2             95   None
447                        next           ∅-2             96   None
448                  likelyseat           ∅-2             97   None
449                        act.           ∅-2             98   None
450                       Party           ∅-2             99   None
451                     pr?vide           ∅-2            100   None
452                                       ∅-2            101   None
453                     surface           ∅-2            102   None
454            industrysecti?n.           ∅-2            103   None
455                    Official           ∅-2            104   None
456                                       ∅-2            105   None
457                       m?del           ∅-2            106   None
458                inv?lvesh?rt           ∅-2            107   None
459                        Mrs.           ∅-2            108   None
460                        F??d           ∅-2            109   None
461                    increase           ∅-2            110   None
462                        film           ∅-2            111   None
463                                       ∅-2            112   None
464                       stand           ∅-2            113   None
465                  t?ughs?rt.           ∅-2            114   None
466                                       ∅-2            115   None
467                       M?ney           ∅-2            116   None
468                pr?duce?ther           ∅-2            117   None
469                                       ∅-2            118   None
470            carrything.Fl??r           ∅-2            119   None
471                                       ∅-2            120   None
472                       scene           ∅-2            121   None
473                          in           ∅-2            122   None
474                  caseheart.           ∅-2            123   None
475                                       ∅-2            124   None
476                Pr?videt?day           ∅-2            125   None
477                    appr?ach           ∅-2            126   None
478                                       ∅-2            127   None
479                         gun           ∅-2            128   None
480                     inside.           ∅-2            129   None
481                      Rep?rt           ∅-2            130   None
482               s?ngread.Bill           ∅-2            131   None
483                                       ∅-2            132   None
484                      debate           ∅-2            133   None
485                       ahead           ∅-2            134   None
486                         n?r           ∅-2            135   None
487                 middlestill           ∅-2            136   None
488                                       ∅-2            137   None
489        participantaudience.           ∅-2            138   None
490                                       ∅-2            139   None
491                         End           ∅-2            140   None
492                  w?uldv?ice           ∅-2            141   None
493                                       ∅-2            142   None
494                 seaAmerican           ∅-2            143   None
495                     because           ∅-2            144   None
496                    quickly.           ∅-2            145   None
497                         Any           ∅-2            146   None
498                        drug           ∅-2            147   None
499                                       ∅-2            148   None
500         scenedevel?p.Market           ∅-2            149   None
501                     science           ∅-2            150   None
502                                       ∅-2            151   None
503                    appr?ach           ∅-2            152   None
504                         me.           ∅-2            153   None
505                       Since           ∅-2            154   None
506                       maj?r           ∅-2            155   None
507                         Mrs           ∅-2            156   None
508               with?utw?rker           ∅-2            157   None
509                                       ∅-2            158   None
510             subject.Teacher           ∅-2            159   None
511                   educati?n           ∅-2            160   None
512                     similar           ∅-2            161   None
513                        race           ∅-2            162   None
514                                       ∅-2            163   None
515                       keep.           ∅-2            164   None
516                    Tw?guess           ∅-2            165   None
517                                       ∅-2            166   None
518              w?nderpr?bably           ∅-2            167   None
519                         bit           ∅-2            168   None
520                      p?licy           ∅-2            169   None
521                 sea.Netw?rk   join.N_twork           170   93  
522                 sea.Netw?rk           ∅-2            170   None
523                                       ∅-2            171   None
524           envir?nmentaffect   aff_ct                 172   95  
525           envir?nmentaffect   _nvironm_nt            172   94  
526                    hist?ry.   history.               173   96  
527                    hist?ry.           ∅-2            173   None
528                               history.               174   96  
529                  V?iceav?id   avoid                  175   98  
530                  V?iceav?id   Voic_                  175   97  
531                        sing   sing                   176   99  
532                        sing           ∅-2            176   None
533                               sing                   177   99  
534                      sec?nd   s_cond                 178   100 
535                         l?t   lot                    179   101 
536               lightthe.Call   light                  180   102 
537               lightthe.Call   th_.Call               180   103 
538                          be   b_                     181   104 
539                       blue.   blu_.                  182   105 
540                    M?vement   Mov_m_nt               183   106 
541                    M?vement           ∅-2            183   None
542                               Mov_m_nt               184   106 
543                       peace   p_ac_                  185   107 
544                        ?pen   op_n                   186   108 
545                  fishm?ther   fish                   187   109 
546                  fishm?ther           ∅-2            187   None
547                  fishm?ther   moth_r                 187   110 
548                               moth_r                 188   110 
549                 air.Prevent   Pr_v_nt                189   112 
550                 air.Prevent   air.                   189   111 
551                     century           ∅-2            190   None
552                     century   c_ntury                190   113 
553                               c_ntury                191   113 
554                     r?leeye   rol_                   192   114 
555                     r?leeye   _y_                    192   115 
556                    analysis   analysis               193   116 
557                      first.   first.                 194   117 
558                     N?thing           ∅-2            195   None
559                     N?thing   Nothing                195   118 
560                               Nothing                196   118 
561                       th?se   thos_                  197   119 
562                  well.Chair           ∅-2            198   None
563                  well.Chair   Chair                  198   121 
564                  well.Chair   w_ll.                  198   120 
565                               Chair                  199   121 
566                       ?ffer   off_r                  200   122 
567               thr?ughseas?n   s_ason                 201   124 
568               thr?ughseas?n   through                201   123 
569                     similar           ∅-2            202   None
570                     similar   similar                202   125 
571                               similar                203   125 
572          necessary.Rulelike   n_c_ssary.Rul_         204   126 
573          necessary.Rulelike   lik_                   204   127 
574                               _ls_                   205   128 
575                   elsedata.           ∅-2            206   None
576                   elsedata.   _ls_                   206   128 
577                   elsedata.   data.                  206   129 
578                               data.                  207   129 
579                     P?pular   Popular                208   130 
580                 enterafter.   aft_r.                 209   132 
581                 enterafter.           ∅-2            209   None
582                 enterafter.   _nt_r                  209   131 
583                               aft_r.                 210   132 
584                          Pm   Pm                     211   133 
585            citizenimp?rtant   important              212   135 
586            citizenimp?rtant   citiz_n                212   134 
587            citizenimp?rtant           ∅-2            212   None
588                               important              213   135 
589                      ?pti?n   option                 214   136 
590                    seethese   th_s_                  215   138 
591                    seethese   s__                    215   137 
592                    seethese           ∅-2            215   None
593                               th_s_                  216   138 
594                     effect.   _ff_ct.                217   139 
595                   Usesh?uld   Us_                    218   140 
596                   Usesh?uld   should                 218   141 
597                     believe   b_li_v_                219   142 
598                               go.                    220   143 
599                     g?.Team   go.                    221   143 
600                     g?.Team   T_am                   221   144 
601                      return   r_turn                 222   145 
602                      chance   chanc_                 223   146 
603                       gr?up   group                  224   147 
604                      d?ct?r   doctor                 225   148 
605                    activity   activity               226   149 
606                    activity           ∅-2            226   None
607                               activity               227   149 
608                       five.   fiv_.                  228   150 
609                  Reduceweek   w__k                   229   152 
610                  Reduceweek           ∅-2            229   None
611                  Reduceweek   R_duc_                 229   151 
612                               w__k                   230   152 
613                    newsdrug   n_ws                   231   153 
614                    newsdrug   drug                   231   154 
615                        time           ∅-2            232   None
616                        time   tim_                   232   155 
617                               tim_                   233   155 
618          m?ve.Businessav?id           ∅-2            234   None
619          m?ve.Businessav?id   mov_.Eat               234   156 
620                       again           ∅-2            235   None
621                                       ∅-2            236   None
622                businessb?y.           ∅-2            237   None
623                       Crime           ∅-2            238   None
624                        live           ∅-2            239   None
625                     n?thing           ∅-2            240   None
626                                       ∅-2            241   None
627                      agency           ∅-2            242   None
628                        h?w.           ∅-2            243   None
629           Missi?npr?ducti?n           ∅-2            244   None
630                                       ∅-2            245   None
631                      system           ∅-2            246   None
632                     reality           ∅-2            247   None
633              reveal.Himself           ∅-2            248   None
634                                       ∅-2            249   None
635                 degreeearly           ∅-2            250   None
636                  garden.Eat           ∅-2            251   None
637                  garden.Eat   mov_.Eat               251   156 
638                        ?nly   only                   252   157 
639                        y?ur   your                   253   158 
640                        y?ur           ∅-2            253   None
641                               your                   254   158 
642                  f?rmer?nly   form_r                 255   159 
643                  f?rmer?nly   only                   255   160 
644                  f?rmer?nly           ∅-2            255   None
645                               only                   256   160 
646                    pr?ject.   proj_ct.               257   161 
647                       Music   Music                  258   162 
648                       ab?ve   abov_                  259   163 
649                       still   still                  260   164 
650                 itselfhelp.   h_lp.                  261   166 
651                 itselfhelp.   its_lf                 261   165 
652                       Clear           ∅-2            262   None
653                       Clear   Cl_ar                  262   167 
654                               Cl_ar                  263   167 
655                 threatahead   thr_at                 264   168 
656                 threatahead   ah_ad                  264   169 
657                                       ∅-2            265   None
658                    evidence   _vid_nc_               266   170 
659          necessaryanything.   anything.              267   172 
660          necessaryanything.   n_c_ssary              267   171 
661                         His           ∅-2            268   None
662                         His   His                    268   173 
663                               His                    269   173 
664                      wind?w   window                 270   174 
665                      ready.   r_ady.                 271   175 
666               Leastanything   L_ast                  272   176 
667               Leastanything   anything               272   177 
668                      the?ry   th_ory                 273   178 
669                      bey?nd   b_yond                 274   179 
670         h?wever.Perf?rmance   how_v_r.P_rformanc_    275   180 
671         h?wever.Perf?rmance           ∅-2            275   None
672                               how_v_r.P_rformanc_    276   180 
673           magazineattenti?n   att_ntion              277   182 
674           magazineattenti?n   magazin_               277   181 
675           magazineattenti?n           ∅-2            277   None
676                               att_ntion              278   182 
677                          ?k   ok                     279   183 
678                    describe   d_scrib_               280   184 
679               ?ffdirecti?n.   off                    281   185 
680               ?ffdirecti?n.   dir_ction.             281   186 
681                      Meth?d   M_thod                 282   187 
682                        give           ∅-2            283   None
683                        give   giv_                   283   188 
684                               giv_                   284   188 
685                       s?uth   south                  285   189 
686                      weight   w_ight                 286   190 
687                      c?urt.   court.                 287   191 
688                Whetherh?use   Wh_th_r                288   192 
689                Whetherh?use   hous_                  288   193 
690                Whetherh?use           ∅-2            288   None
691                               hous_                  289   193 
692                       fight   fight                  290   194 
693                       plant   plant                  291   195 
694                     devel?p   d_v_lop                292   196 
695          ?fficial.L?sst?tal   total                  293   198 
696          ?fficial.L?sst?tal   official.Loss          293   197 
697                     weight.   w_ight.                294   199 
698                     weight.           ∅-2            294   None
699                               w_ight.                295   199 
700                       Sp?rt   Sport                  296   200 
701               whethereffect   _ff_ct                 297   202 
702               whethereffect   wh_th_r                297   201 
703                     t?ward.   toward.                298   203 
704                     Himself   Hims_lf                299   204 
705                     Himself           ∅-2            299   None
706                               Hims_lf                300   204 
707                st?refinally   finally                301   206 
708                st?refinally   stor_                  301   205 
709                st?refinally           ∅-2            301   None
710                               finally                302   206 
711                       ?ver.   ov_r.                  303   207 
712                       Stand   Stand                  304   208 
713                  tw?s?me?ne   two                    305   209 
714                  tw?s?me?ne   som_on_                305   210 
715                          Mr   Mr                     306   211 
716                          Mr           ∅-2            306   None
717                               Mr                     307   211 
718                     pr?cess   proc_ss                308   212 
719              bagc?ach.Write   bag                    309   213 
720              bagc?ach.Write   coach.Writ_            309   214 
721                      bec?me   b_com_                 310   215 
722                      bec?me           ∅-2            310   None
723                               b_com_                 311   215 
724                 v?icegarden   gard_n                 312   217 
725                 v?icegarden           ∅-2            312   None
726                 v?icegarden   voic_                  312   216 
727                               gard_n                 313   217 
728               p?sitive.Such   positiv_.              314   218 
729               p?sitive.Such   Such                   314   219 
730                     c?ntain           ∅-2            315   None
731                     c?ntain   contain                315   220 
732                               contain                316   220 
733                    fullwh?m   whom                   317   222 
734                    fullwh?m   full                   317   221 
735                         wh?   who                    318   223 
736                       m?vie   movi_                  319   224 
737                       m?vie           ∅-2            319   None
738                               movi_                  320   224 
739                    per.Thus           ∅-2            321   None
740                    per.Thus   Thus                   321   226 
741                    per.Thus   p_r.                   321   225 
742                               Thus                   322   226 
743                    material   mat_rial               323   227 
744                      nati?n   nation                 324   228 
745                          us   us                     325   229 
746                     address   addr_ss                326   230 
747          sensey?urself.Fire   yours_lf.Fir_          327   232 
748          sensey?urself.Fire           ∅-2            327   None
749          sensey?urself.Fire   s_ns_                  327   231 
750                               yours_lf.Fir_          328   232 
751                        ?pen   op_n                   329   233 
752                         but   but                    330   234 
753      envir?nmentalinterview   int_rvi_w              331   236 
754      envir?nmentalinterview   _nvironm_ntal          331   235 
755                      sec?nd   s_cond                 332   237 
756                                       ∅-2            333   None
757                       east.   _ast.                  334   238 
758                  Finalab?ve   abov_                  335   240 
759                  Finalab?ve   Final                  335   239 
760                   everyb?dy   _v_rybody              336   241 
761                   everyb?dy           ∅-2            336   None
762                               _v_rybody              337   241 
763                        type   typ_                   338   242 
764               after.Pr?duce   aft_r.                 339   243 
765               after.Pr?duce   Produc_                339   244 
766                        b?dy   body                   340   245 
767                        b?dy           ∅-2            340   None
768                               body                   341   245 
769                     inv?lve   involv_                342   246 
770                      nearly   n_arly                 343   247 
771                m?delbetween   mod_l                  344   248 
772                m?delbetween   b_tw__n                344   249 
773                      m?del.   mod_l.                 345   250 
774                      m?del.           ∅-2            345   None
775                               mod_l.                 346   250 
776                    Business   Busin_ss               347   251 
777                        miss   miss                   348   252 
778                       image   imag_                  349   253 
779                         TV.   TV.                    350   254 
780                          S?   So                     351   255 
781               prettydevel?p   d_v_lop                352   257 
782               prettydevel?p   pr_tty                 352   256 
783               prettydevel?p           ∅-2            352   None
784                               d_v_lop                353   257 
785                     current   curr_nt                354   258 
786                part.Service   part.S_rvic_           355   259 
787                   difficult   difficult              356   260 
788                 currentskin           ∅-2            357   None
789                 currentskin   skin                   357   262 
790                 currentskin   curr_nt                357   261 
791                               skin                   358   262 
792                    capital.   capital.               359   263 
793                        Fire   Fir_                   360   264 
794                   deepprice   pric_                  361   266 
795                   deepprice   d__p                   361   265 
796                   deepprice           ∅-2            361   None
797                               pric_                  362   266 
798                         buy   buy                    363   267 
799                    pressure   pr_ssur_               364   268 
800                    s?meb?dy   som_body               365   269 
801                     teacher   t_ach_r                366   270 
802        gr?wth.Y?urselfsc?re   scor_                  367   272 
803        gr?wth.Y?urselfsc?re   growth.Yours_lf        367   271 
804                          ?n           ∅-2            368   None
805                          ?n   on                     368   273 
806                               on                     369   273 
807               createmissi?n   cr_at_                 370   274 
808               createmissi?n   mission                370   275 
809                     middle.   middl_.                371   276 
810                  C?llecti?n   Coll_ction             372   277 
811                               off_r                  373   278 
812                    ?fferadd   off_r                  374   278 
813                    ?fferadd   add                    374   279 
814                        item   it_m                   375   280 
815                        item           ∅-2            375   None
816                               it_m                   376   280 
817                     citizen   citiz_n                377   281 
818                   writeaway   away                   378   283 
819                   writeaway   writ_                  378   282 
820                     career.           ∅-2            379   None
821                     career.   car__r.                379   284 
822                               car__r.                380   284 
823                   Talkwater   Talk                   381   285 
824                   Talkwater   wat_r                  381   286 
825                ?rganizati?n           ∅-2            382   None
826                ?rganizati?n   organization           382   287 
827                               organization           383   287 
828                message.Step           ∅-2            384   None
829                message.Step   m_ssag_.               384   288 
830                message.Step   St_p                   384   289 
831                               St_p                   385   289 
832                      risebe   ris_                   386   290 
833                      risebe   b_                     386   291 
834                               b_                     387   291 
835                         age   ag_                    388   292 
836                ec?n?my.Yeah   _conomy.R_gion         389   293 
837                ec?n?my.Yeah           ∅-2            389   None
838                   ?wnsummer           ∅-2            390   None
839                                       ∅-2            391   None
840                   sh?rtfive           ∅-2            392   None
841                       seek.           ∅-2            393   None
842                        L??k           ∅-2            394   None
843                                       ∅-2            395   None
844                   f??tcause           ∅-2            396   None
845                          t?           ∅-2            397   None
846                                       ∅-2            398   None
847                       maybe           ∅-2            399   None
848                       right           ∅-2            400   None
849                   magazine.           ∅-2            401   None
850                         Car           ∅-2            402   None
851                     exactly           ∅-2            403   None
852                     devel?p           ∅-2            404   None
853                     s?ciety           ∅-2            405   None
854                       cause           ∅-2            406   None
855                          we           ∅-2            407   None
856                          by           ∅-2            408   None
857                   s?ng.G??d           ∅-2            409   None
858                  discussi?n           ∅-2            410   None
859                                       ∅-2            411   None
860                h?spitalpick           ∅-2            412   None
861                                       ∅-2            413   None
862                least.Camera           ∅-2            414   None
863               increasefr?nt           ∅-2            415   None
864                                       ∅-2            416   None
865                        site           ∅-2            417   None
866                     p?pular           ∅-2            418   None
867               appr?achrest.           ∅-2            419   None
868                     Finally           ∅-2            420   None
869                     realize           ∅-2            421   None
870                                       ∅-2            422   None
871                   certainly           ∅-2            423   None
872                ?fficialf?ur           ∅-2            424   None
873                                       ∅-2            425   None
874                 n?r.Defense           ∅-2            426   None
875                                       ∅-2            427   None
876                        wind           ∅-2            428   None
877                willsurface.           ∅-2            429   None
878                         Cup           ∅-2            430   None
879                                       ∅-2            431   None
880                          PM           ∅-2            432   None
881                     feeling           ∅-2            433   None
882                  dem?cratic           ∅-2            434   None
883                 thr?ughf?ur           ∅-2            435   None
884                which.Regi?n           ∅-2            436   None
885                which.Regi?n   _conomy.R_gion         436   293 
886                       range           ∅-2            437   None
887                       range   rang_                  437   294 
888                               rang_                  438   294 
889                        f??t   foot                   439   295 
890                    article.   articl_.               440   296 
891                 Ag?actually   actually               441   298 
892                 Ag?actually   Ago                    441   297 
893                     secti?n           ∅-2            442   None
894                     secti?n   s_ction                442   299 
895                               s_ction                443   299 
896          activity.Executive   Ex_cutiv_              444   301 
897          activity.Executive   activity.              444   300 
898                    security   s_curity               445   302 
899                    security           ∅-2            445   None
900                               s_curity               446   302 
901                 cardchance.   chanc_.                447   304 
902                 cardchance.   card                   447   303 
903                       Music   Music                  448   305 
904                     defense           ∅-2            449   None
905                     defense   d_f_ns_                449   306 
906                               d_f_ns_                450   306 
907              c?llegepr?ject   proj_ct                451   308 
908              c?llegepr?ject   coll_g_                451   307 
909                        sell           ∅-2            452   None
910                        sell   s_ll                   452   309 
911                               s_ll                   453   309 
912                     little.   littl_.                454   310 
913                    St?pc?st   Stop                   455   311 
914                    St?pc?st   cost                   455   312 
915                 c?mm?n.Card           ∅-2            456   None
916                 c?mm?n.Card   common.Card            456   313 
917                               common.Card            457   313 
918              successfulthan   than                   458   315 
919              successfulthan   succ_ssful             458   314 
920                       human   human                  459   316 
921                       human           ∅-2            459   None
922                               human                  460   316 
923                  yetreflect   r_fl_ct                461   318 
924                  yetreflect   y_t                    461   317 
925                     inside.   insid_.                462   319 
926                       Crime           ∅-2            463   None
927                       Crime   Crim_                  463   320 
928                               Crim_                  464   320 
929                         ?wn   own                    465   321 
930             am?unty?urself.   yours_lf.              466   323 
931             am?unty?urself.   amount                 466   322 
932                      P?licy   Policy                 467   324 
933                       wh?se   whos_                  468   325 
934                     h?wever   how_v_r                469   326 
935                       issue           ∅-2            470   None
936                       issue   issu_                  470   327 
937                               issu_                  471   327 
938                     w?rker.   work_r.                472   328 
939                      Entire   Entir_                 473   329 
940            despitestatement   stat_m_nt              474   331 
941            despitestatement           ∅-2            474   None
942            despitestatement   d_spit_                474   330 
943                               stat_m_nt              475   331 
944                  underp?wer   pow_r                  476   333 
945                  underp?wer           ∅-2            476   None
946                  underp?wer   und_r                  476   332 
947                               pow_r                  477   333 
948              freec?ach.Firm   coach.Firm             478   335 
949              freec?ach.Firm           ∅-2            478   None
950              freec?ach.Firm   fr__                   478   334 
951                               coach.Firm             479   335 
952                         ?ld   old                    480   336 
953               mediamaintain   m_dia                  481   337 
954               mediamaintain   maintain               481   338 
955                 Republican.           ∅-2            482   None
956                 Republican.   R_publican.            482   339 
957                               R_publican.            483   339 
958                        East   East                   484   340 
959                   restpiece   pi_c_                  485   342 
960                   restpiece   r_st                   485   341 
961                   restpiece           ∅-2            485   None
962                               pi_c_                  486   342 
963                   campaign.   campaign.              487   343 
964                  Nextletter   N_xt                   488   344 
965                  Nextletter   l_tt_r                 488   345 
966                       l?cal   local                  489   346 
967                       still   still                  490   347 
968                  set.Family   s_t.Family             491   348 
969                         arm   arm                    492   349 
970              administrati?n           ∅-2            493   None
971              administrati?n   administration         493   350 
972                               administration         494   350 
973                th?ught.What   thought.               495   351 
974                th?ught.What           ∅-2            495   None
975                th?ught.What   What                   495   352 
976                               What                   496   352 
977                 feelbr?ther   f__l                   497   353 
978                 feelbr?ther   broth_r                497   354 
979                      n?tice   notic_                 498   355 
980                       fill.           ∅-2            499   None
981                       fill.   fill.                  499   356 
982                               fill.                  500   356 
983                 Any?neab?ve   Anyon_                 501   357 
984                 Any?neab?ve   abov_                  501   358 
985                       pr?ve   prov_                  502   359 
986                         see   s__                    503   360 
987                         see           ∅-2            503   None
988                               s__                    504   360 
989                     f?reign   for_ign                505   361 
990                    measure.   m_asur_.               506   362 
991                        Side   Sid_                   507   363 
992                    haver??m   room                   508   365 
993                    haver??m   hav_                   508   364 
994                     pr?duct   product                509   366 
995                         l?w   low                    510   367 
996                c?ntain.Past   contain.Past           511   368 
997                      n?tice   notic_                 512   369 
998                      bec?me           ∅-2            513   None
999                      bec?me   b_com_                 513   370 
1000                              b_com_                 514   370 
1001                 star.Where   star.                  515   371 
1002                 star.Where   Wh_r_                  515   372 
1003                          I   I                      516   373 
1004                       time   tim_                   517   374 
1005                     animal   animal                 518   375 
1006                     animal           ∅-2            518   None
1007                              animal                 519   375 
1008           theminclude.Five   includ_.Bit            520   377 
1009           theminclude.Five   th_m                   520   376 
1010           theminclude.Five           ∅-2            520   None
1011                       seem           ∅-2            521   None
1012                                      ∅-2            522   None
1013                 planreturn           ∅-2            523   None
1014                       ?ver           ∅-2            524   None
1015                      c?ver           ∅-2            525   None
1016                     plant.           ∅-2            526   None
1017                       Game           ∅-2            527   None
1018                    present           ∅-2            528   None
1019                       that           ∅-2            529   None
1020                                      ∅-2            530   None
1021                     camera           ∅-2            531   None
1022                       skin           ∅-2            532   None
1023                    teamt??           ∅-2            533   None
1024                   pr?tect.           ∅-2            534   None
1025                        Him           ∅-2            535   None
1026                        cut           ∅-2            536   None
1027                                      ∅-2            537   None
1028                 chargeyear           ∅-2            538   None
1029                                      ∅-2            539   None
1030              pressured?wn.           ∅-2            540   None
1031                                      ∅-2            541   None
1032                        Off           ∅-2            542   None
1033                ?ldcampaign           ∅-2            543   None
1034                        yet           ∅-2            544   None
1035                                      ∅-2            545   None
1036             true.Auth?rity           ∅-2            546   None
1037            establishfinish           ∅-2            547   None
1038                                      ∅-2            548   None
1039            surfacenetw?rk.           ∅-2            549   None
1040                       Firm           ∅-2            550   None
1041                                      ∅-2            551   None
1042                all?wstr?ng           ∅-2            552   None
1043                                      ∅-2            553   None
1044               m?resuggest.           ∅-2            554   None
1045                                      ∅-2            555   None
1046                      S?uth           ∅-2            556   None
1047                daughterf?r           ∅-2            557   None
1048                      black           ∅-2            558   None
1049                                      ∅-2            559   None
1050                      still           ∅-2            560   None
1051                      g?al.           ∅-2            561   None
1052             Supp?rtmachine           ∅-2            562   None
1053                                      ∅-2            563   None
1054               g?treatment.           ∅-2            564   None
1055                       Rest           ∅-2            565   None
1056                      apply           ∅-2            566   None
1057                       idea           ∅-2            567   None
1058                    inv?lve           ∅-2            568   None
1059                                      ∅-2            569   None
1060                measure.Bit   includ_.Bit            570   377 
1061                measure.Bit           ∅-2            570   None
1062                       team   t_am                   571   378 
1063                  r??mfield   room                   572   379 
1064                  r??mfield   fi_ld                  572   380 
1065                    address   addr_ss                573   381 
1066                  analysis.           ∅-2            574   None
1067                  analysis.   analysis.              574   382 
1068                              analysis.              575   382 
1069                    Secti?n   S_ction                576   383 
1070                      ?ccur   occur                  577   384 
1071                     remain   r_main                 578   385 
1072                       fill   fill                   579   386 
1073               imagine.H?me           ∅-2            580   None
1074               imagine.H?me   Hom_                   580   388 
1075               imagine.H?me   imagin_.               580   387 
1076                              Hom_                   581   388 
1077                  resp?ndt?   to                     582   390 
1078                  resp?ndt?   r_spond                582   389 
1079                  available   availabl_              583   391 
1080                      ready   r_ady                  584   392 
1081                    appear.           ∅-2            585   None
1082                    appear.   app_ar.                585   393 
1083                              app_ar.                586   393 
1084               Agreec?llege   coll_g_                587   395 
1085               Agreec?llege   Agr__                  587   394 
1086                      three   thr__                  588   396 
1087                      three           ∅-2            588   None
1088                              thr__                  589   396 
1089               already.Fine   Fin_                   590   398 
1090               already.Fine           ∅-2            590   None
1091               already.Fine   alr_ady.               590   397 
1092                              Fin_                   591   398 
1093      past?rganizati?n.Late   organization.Lat_      592   400 
1094      past?rganizati?n.Late   past                   592   399 
1095                       hear   h_ar                   593   401 
1096                       hear           ∅-2            593   None
1097                              h_ar                   594   401 
1098                       size   siz_                   595   402 
1099                   whatever   what_v_r               596   403 
1100                  miss.Trip   Trip                   597   405 
1101                  miss.Trip   miss.                  597   404 
1102                   language           ∅-2            598   None
1103                   language   languag_               598   406 
1104                              languag_               599   406 
1105              bestinterview   b_st                   600   407 
1106              bestinterview   int_rvi_w              600   408 
1107             envir?nmental.   _nvironm_ntal.         601   409 
1108             envir?nmental.           ∅-2            601   None
1109                              _nvironm_ntal.         602   409 
1110               Cameralisten   Cam_ra                 603   410 
1111               Cameralisten   list_n                 603   411 
1112                     eff?rt   _ffort                 604   412 
1113                   military           ∅-2            605   None
1114                   military   military               605   413 
1115                              military               606   413 
1116                 m?mentseek   mom_nt                 607   414 
1117                 m?mentseek   s__k                   607   415 
1118                                      ∅-2            608   None
1119               else.Hundred   _ls_.Hundr_d           609   416 
1120              andp?pulati?n           ∅-2            610   None
1121              andp?pulati?n   and                    610   417 
1122              andp?pulati?n   population             610   418 
1123                              population             611   418 
1124             c?llecti?nkind   kind                   612   420 
1125             c?llecti?nkind           ∅-2            612   None
1126             c?llecti?nkind   coll_ction             612   419 
1127                              kind                   613   420 
1128                  call.Push   call.                  614   421 
1129                  call.Push   Push                   614   422 
1130                        yet   y_t                    615   423 
1131                              t_ll                   616   424 
1132                  tellagree   t_ll                   617   424 
1133                  tellagree   agr__                  617   425 
1134                    sch??l.   school.                618   426 
1135                     P?lice   Polic_                 619   427 
1136                      issue           ∅-2            620   None
1137                      issue   issu_                  620   428 
1138                              issu_                  621   428 
1139               bef?re.Crime           ∅-2            622   None
1140               bef?re.Crime   b_for_.                622   429 
1141               bef?re.Crime   Crim_                  622   430 
1142                              Crim_                  623   430 
1143             w?rdtechn?l?gy   t_chnology             624   432 
1144             w?rdtechn?l?gy   word                   624   431 
1145                        yes   y_s                    625   433 
1146                     n?tice   notic_                 626   434 
1147                     reveal           ∅-2            627   None
1148                     reveal   r_v_al                 627   435 
1149                              r_v_al                 628   435 
1150               benefit.Need   b_n_fit.N__d           629   436 
1151                 relatewell   r_lat_                 630   437 
1152                 relatewell           ∅-2            630   None
1153                 relatewell   w_ll                   630   438 
1154                              w_ll                   631   438 
1155                     matter   matt_r                 632   439 
1156                  dr?p.Draw   drop.                  633   440 
1157                  dr?p.Draw   Draw                   633   441 
1158                       f?rm   form                   634   442 
1159                       f?rm           ∅-2            634   None
1160                              form                   635   442 
1161                 stuffhead.           ∅-2            636   None
1162                 stuffhead.   h_ad.                  636   444 
1163                 stuffhead.   stuff                  636   443 
1164                              h_ad.                  637   444 
1165                Staffrep?rt   Staff                  638   445 
1166                Staffrep?rt   r_port                 638   446 
1167                Staffrep?rt           ∅-2            638   None
1168                              r_port                 639   446 
1169                        may   may                    640   447 
1170                     b?thd?   do                     641   449 
1171                     b?thd?   both                   641   448 
1172                   billi?n.           ∅-2            642   None
1173                   billi?n.   billion.               642   450 
1174                              billion.               643   450 
1175                   Cust?mer   Custom_r               644   451 
1176                        red   r_d                    645   452 
1177               fearth?usand   thousand               646   454 
1178               fearth?usand   f_ar                   646   453 
1179                              l_t                    647   455 
1180                 lett?night   tonight                648   456 
1181                 lett?night   l_t                    648   455 
1182                              s__m.                  649   457 
1183                  seem.L?ng   s__m.                  650   457 
1184                  seem.L?ng           ∅-2            650   None
1185                  seem.L?ng   Long                   650   458 
1186                              Long                   651   458 
1187                      sh?rt   short                  652   459 
1188                     recent   r_c_nt                 653   460 
1189                      c?uld   could                  654   461 
1190           stuffstudent.The   stud_nt.Drop           655   463 
1191           stuffstudent.The   stuff                  655   462 
1192           stuffstudent.The           ∅-2            655   None
1193                       case           ∅-2            656   None
1194                     garden           ∅-2            657   None
1195                                      ∅-2            658   None
1196                      start           ∅-2            659   None
1197               kn?wnati?nal           ∅-2            660   None
1198                      while           ∅-2            661   None
1199                    gr?wth.           ∅-2            662   None
1200                                      ∅-2            663   None
1201                 Winf?rward           ∅-2            664   None
1202                      ahead           ∅-2            665   None
1203                                      ∅-2            666   None
1204                 mindstand.           ∅-2            667   None
1205                                      ∅-2            668   None
1206             Discussi?nthen           ∅-2            669   None
1207                    citizen           ∅-2            670   None
1208                gr?wth.T?wn           ∅-2            671   None
1209                                      ∅-2            672   None
1210                  celladult           ∅-2            673   None
1211                                      ∅-2            674   None
1212                career.Card           ∅-2            675   None
1213                                      ∅-2            676   None
1214                  affectwhy           ∅-2            677   None
1215                       card           ∅-2            678   None
1216                    w?nder.           ∅-2            679   None
1217                                      ∅-2            680   None
1218                Alm?stcheck           ∅-2            681   None
1219                                      ∅-2            682   None
1220                         t?           ∅-2            683   None
1221                  ?perati?n           ∅-2            684   None
1222                       push           ∅-2            685   None
1223                     clear.           ∅-2            686   None
1224                       F?rm           ∅-2            687   None
1225             spendstandard.           ∅-2            688   None
1226                                      ∅-2            689   None
1227            Behindimp?rtant           ∅-2            690   None
1228                                      ∅-2            691   None
1229             buildingsch??l           ∅-2            692   None
1230                                      ∅-2            693   None
1231            p?sitive.Gr?wth           ∅-2            694   None
1232                   increase           ∅-2            695   None
1233                event.Watch           ∅-2            696   None
1234                                      ∅-2            697   None
1235              fl??rh?spital           ∅-2            698   None
1236                                      ∅-2            699   None
1237                        few           ∅-2            700   None
1238                    century           ∅-2            701   None
1239              include.Crime           ∅-2            702   None
1240                                      ∅-2            703   None
1241           blue?rganizati?n           ∅-2            704   None
1242                                      ∅-2            705   None
1243                        and           ∅-2            706   None
1244         g??d.Dr?pincluding   stud_nt.Drop           707   463 
1245         g??d.Dr?pincluding   including              707   464 
1246         g??d.Dr?pincluding           ∅-2            707   None
1247                              including              708   464 
1248             causebeautiful   caus_                  709   465 
1249             causebeautiful   b_autiful              709   466 
1250                      pr?ve   prov_                  710   467 
1251                      pr?ve           ∅-2            710   None
1252                              prov_                  711   467 
1253                    system.   syst_m.                712   468 
1254                Believecare   car_                   713   470 
1255                Believecare   B_li_v_                713   469 
1256                        n?w           ∅-2            714   None
1257                        n?w   now                    714   471 
1258                              now                    715   471 
1259            myc?mputer.Less   my                     716   472 
1260            myc?mputer.Less   comput_r.L_ss          716   473 
1261                  agreement   agr__m_nt              717   474 
1262                      range   rang_                  718   475 
1263                      dream   dr_am                  719   476 
1264                      dream           ∅-2            719   None
1265                              dr_am                  720   476 
1266                   picture.   pictur_.               721   477 
1267                    Taxpart   part                   722   479 
1268                    Taxpart   Tax                    722   478 
1269                    Taxpart           ∅-2            722   None
1270                              part                   723   479 
1271             candidatepaper   candidat_              724   480 
1272             candidatepaper   pap_r                  724   481 
1273                      build   build                  725   482 
1274                      build           ∅-2            725   None
1275                              build                  726   482 
1276                        add   add                    727   483 
1277                  different   diff_r_nt              728   484 
1278               f?ll?w.Plant           ∅-2            729   None
1279               f?ll?w.Plant   Plant                  729   486 
1280               f?ll?w.Plant   follow.                729   485 
1281                              Plant                  730   486 
1282                   anything   anything               731   487 
1283                  c?l?rb??k   color                  732   488 
1284                  c?l?rb??k   book                   732   489 
1285                   l?ng.Arm   long.Arm               733   490 
1286                   l?ng.Arm           ∅-2            733   None
1287                              long.Arm               734   490 
1288                       v?te   vot_                   735   491 
1289              c?nsiderseat.   s_at.                  736   493 
1290              c?nsiderseat.   consid_r               736   492 
1291                    Inv?lve   Involv_                737   494 
1292                    Inv?lve           ∅-2            737   None
1293                              Involv_                738   494 
1294                      y?ung   young                  739   495 
1295                readyspeech   sp__ch                 740   497 
1296                readyspeech   r_ady                  740   496 
1297                                      ∅-2            741   None
1298            entirestandard.   _ntir_                 742   498 
1299            entirestandard.   standard.              742   499 
1300            entirestandard.           ∅-2            742   None
1301                              standard.              743   499 
1302                 Opengarden   Op_n                   744   500 
1303                 Opengarden   gard_n                 744   501 
1304                 Opengarden           ∅-2            744   None
1305                              gard_n                 745   501 
1306                dreamdetail   d_tail                 746   503 
1307                dreamdetail   dr_am                  746   502 
1308                dreamdetail           ∅-2            746   None
1309                              d_tail                 747   503 
1310                 ab?utwait.   about                  748   504 
1311                 ab?utwait.   wait.                  748   505 
1312                 ab?utwait.           ∅-2            748   None
1313                              wait.                  749   505 
1314                    Believe   B_li_v_                750   506 
1315                 ?thersb?dy   oth_rs                 751   507 
1316                 ?thersb?dy   body                   751   508 
1317                      under   und_r                  752   509 
1318                   m?vement   mov_m_nt               753   510 
1319                        TV.   TV.                    754   511 
1320                       Talk   Talk                   755   512 
1321                       Talk           ∅-2            755   None
1322                              Talk                   756   512 
1323                  newsapply   apply                  757   514 
1324                  newsapply   n_ws                   757   513 
1325                  newsapply           ∅-2            757   None
1326                              apply                  758   514 
1327               parentexpert   par_nt                 759   515 
1328               parentexpert   _xp_rt                 759   516 
1329                                      ∅-2            760   None
1330             effectwalk.She           ∅-2            761   None
1331             effectwalk.She   _ff_ct                 761   517 
1332             effectwalk.She   walk.Sh_               761   518 
1333                              walk.Sh_               762   518 
1334                    picture   pictur_                763   519 
1335               th?ughtthan.   thought                764   520 
1336               th?ughtthan.   than.                  764   521 
1337               th?ughtthan.           ∅-2            764   None
1338                              than.                  765   521 
1339                        Way   Way                    766   522 
1340                afterbring.   bring.                 767   524 
1341                afterbring.   aft_r                  767   523 
1342                       Wait   Wait                   768   525 
1343                    pr?cess           ∅-2            769   None
1344                    pr?cess   proc_ss                769   526 
1345                              proc_ss                770   526 
1346                  auth?rity   authority              771   527 
1347                   henumber   numb_r                 772   529 
1348                   henumber   h_                     772   528 
1349                  kn?wledge   knowl_dg_              773   530 
1350                      head.           ∅-2            774   None
1351                      head.   h_ad.                  774   531 
1352                              h_ad.                  775   531 
1353                    Article   Articl_                776   532 
1354                       part   part                   777   533 
1355                     animal   animal                 778   534 
1356                   p?litics   politics               779   535 
1357                     nati?n   nation                 780   536 
1358                 finalthan.   final                  781   537 
1359                 finalthan.   than.                  781   538 
1360                 finalthan.           ∅-2            781   None
1361                              than.                  782   538 
1362                       Team   T_am                   783   539 
1363                     f?rmer   form_r                 784   540 
1364    crime.Auth?rityAmerican           ∅-2            785   None
1365    crime.Auth?rityAmerican   crim_.Str__t           785   541 
1366                                      ∅-2            786   None
1367              springar?und.           ∅-2            787   None
1368                                      ∅-2            788   None
1369                 Speechsave           ∅-2            789   None
1370                     create           ∅-2            790   None
1371                                      ∅-2            791   None
1372                      trade           ∅-2            792   None
1373                      study           ∅-2            793   None
1374                    p?pular           ∅-2            794   None
1375              perf?rm.Occur           ∅-2            795   None
1376                                      ∅-2            796   None
1377                       play           ∅-2            797   None
1378                  p?intway.           ∅-2            798   None
1379                      Third           ∅-2            799   None
1380                       like           ∅-2            800   None
1381                     chance           ∅-2            801   None
1382                                      ∅-2            802   None
1383                      trade           ∅-2            803   None
1384                r??msch??l.           ∅-2            804   None
1385                        Cup           ∅-2            805   None
1386                 individual           ∅-2            806   None
1387                                      ∅-2            807   None
1388          severalyes.Street   crim_.Str__t           808   541 
1389          severalyes.Street           ∅-2            808   None
1390                   c?mputer           ∅-2            809   None
1391                   c?mputer   comput_r               809   542 
1392                              comput_r               810   542 
1393                     agency   ag_ncy                 811   543 
1394         situati?n.Practice   Practic_               812   545 
1395         situati?n.Practice   situation.             812   544 
1396                    western   w_st_rn                813   546 
1397                       else           ∅-2            814   None
1398                       else   _ls_                   814   547 
1399                              _ls_                   815   547 
1400                 h?weverany   any                    816   549 
1401                 h?weverany   how_v_r                816   548 
1402                     affect   aff_ct                 817   550 
1403                     glass.   glass.                 818   551 
1404                     glass.           ∅-2            818   None
1405                              glass.                 819   551 
1406            Every?nesubject   Ev_ryon_               820   552 
1407            Every?nesubject   subj_ct                820   553 
1408                instituti?n   institution            821   554 
1409                      true.   tru_.                  822   555 
1410                      true.           ∅-2            822   None
1411                              tru_.                  823   555 
1412                      Where   Wh_r_                  824   556 
1413                      white   whit_                  825   557 
1414                       half   half                   826   558 
1415                       left   l_ft                   827   559 
1416                ?pp?rtunity   opportunity            828   560 
1417                   g?allate   goal                   829   561 
1418                   g?allate   lat_                   829   562 
1419                              lat_                   830   562 
1420                attack.S?rt           ∅-2            831   None
1421                attack.S?rt   Sort                   831   564 
1422                attack.S?rt   attack.                831   563 
1423                              Sort                   832   564 
1424                 laydiscuss   discuss                833   566 
1425                 laydiscuss   lay                    833   565 
1426                 laydiscuss           ∅-2            833   None
1427                              discuss                834   566 
1428               ?rder.Expect   ord_r.Exp_ct           835   567 
1429              decadedetail.   d_cad_                 836   568 
1430              decadedetail.   d_tail.                836   569 
1431                       Type   Typ_                   837   570 
1432              internati?nal   int_rnational          838   571 
1433                       side   sid_                   839   572 
1434                      ab?ut           ∅-2            840   None
1435                      ab?ut   about                  840   573 
1436                              about                  841   573 
1437              cultural.Head   H_ad                   842   575 
1438              cultural.Head   cultural.              842   574 
1439              cultural.Head           ∅-2            842   None
1440                              H_ad                   843   575 
1441                         we   w_                     844   576 
1442             st?ryp?litical   political              845   578 
1443             st?ryp?litical   story                  845   577 
1444                     church   church                 846   579 
1445                        act           ∅-2            847   None
1446                        act   act                    847   580 
1447                              act                    848   580 
1448              chairhusband.           ∅-2            849   None
1449              chairhusband.   husband.               849   582 
1450              chairhusband.   chair                  849   581 
1451                              husband.               850   582 
1452              Energythr?ugh   En_rgy                 851   583 
1453              Energythr?ugh   through                851   584 
1454                      stuff   stuff                  852   585 
1455                      wh?le   whol_                  853   586 
1456                         g?   go                     854   587 
1457                     church   church                 855   588 
1458                     church           ∅-2            855   None
1459                              church                 856   588 
1460            cl?se.Sizew?man   clos_.Siz_             857   589 
1461            cl?se.Sizew?man   woman                  857   590 
1462                      smile   smil_                  858   591 
1463                      smile           ∅-2            858   None
1464                              smil_                  859   591 
1465                       even   _v_n                   860   592 
1466                       talk   talk                   861   593 
1467               welln?thing.   w_ll                   862   594 
1468               welln?thing.   nothing.               862   595 
1469                Devel?pment   D_v_lopm_nt            863   596 
1470                          I   I                      864   597 
1471                      table   tabl_                  865   598 
1472                      table           ∅-2            865   None
1473                              tabl_                  866   598 
1474                    subject   subj_ct                867   599 
1475                      type.   typ_.                  868   600 
1476             Presidenth?tel   Pr_sid_nt              869   601 
1477             Presidenth?tel   hot_l                  869   602 
1478                     m?dern   mod_rn                 870   603 
1479                       push           ∅-2            871   None
1480                       push   push                   871   604 
1481                              push                   872   604 
1482                       r??m   room                   873   605 
1483                   ?ther.On   On                     874   607 
1484                   ?ther.On   oth_r.                 874   606 
1485                    milli?n   million                875   608 
1486                    milli?n           ∅-2            875   None
1487                              million                876   608 
1488                         we   w_                     877   609 
1489                expectc?urt   _xp_ct                 878   610 
1490                expectc?urt   court                  878   611 
1491                     relate   r_lat_                 879   612 
1492                    s?ldier   soldi_r                880   613 
1493             p?litical.Tell   political.T_ll         881   614 
1494                     reduce           ∅-2            882   None
1495                     reduce   r_duc_                 882   615 
1496                              r_duc_                 883   615 
1497                 m?therr?le   rol_                   884   617 
1498                 m?therr?le   moth_r                 884   616 
1499                 m?therr?le           ∅-2            884   None
1500                              rol_                   885   617 
1501                   gun.Cell   gun.                   886   618 
1502                   gun.Cell   C_ll                   886   619 
1503                                      ∅-2            887   None
1504               expectanimal   _xp_ct                 888   620 
1505               expectanimal   animal                 888   621 
1506                      stage   stag_                  889   622 
1507                      stage           ∅-2            889   None
1508                              stag_                  890   622 
1509                m?del.Maybe   Mayb_                  891   624 
1510                m?del.Maybe   mod_l.                 891   623 
1511                significant           ∅-2            892   None
1512                significant   significant            892   625 
1513                              significant            893   625 
1514                    benefit   b_n_fit                894   626 
1515                 bank.F?cus   bank.                  895   627 
1516                 bank.F?cus   Focus                  895   628 
1517                    success           ∅-2            896   None
1518                    success   succ_ss                896   629 
1519                              succ_ss                897   629 
1520                  callwatch   call                   898   630 
1521                  callwatch   watch                  898   631 
1522                  callwatch           ∅-2            898   None
1523                              watch                  899   631 
1524               tend.Milli?n   t_nd.                  900   632 
1525               tend.Milli?n   Million                900   633 
1526               tend.Milli?n           ∅-2            900   None
1527                              Million                901   633 
1528                       fast   fast                   902   634 
1529                     rep?rt   r_port                 903   635 
1530                       page   pag_                   904   636 
1531                     trial.   trial.                 905   637 
1532            Identifypr?gram   Id_ntify               906   638 
1533            Identifypr?gram           ∅-2            906   None
1534            Identifypr?gram   program                906   639 
1535                              program                907   639 
1536                        ?ut   out                    908   640 
1537             pull.R??mwatch   pull.Room              909   641 
1538             pull.R??mwatch   watch                  909   642 
1539                        use           ∅-2            910   None
1540                        use   us_                    910   643 
1541                              us_                    911   643 
1542                       wall   wall                   912   644 
1543                       dark   dark                   913   645 
1544                    subject   subj_ct                914   646 
1545                      read.   r_ad.                  915   647 
1546                 Deeprather   rath_r                 916   649 
1547                 Deeprather   D__p                   916   648 
1548                       away   away                   917   650 
1549                      music   music                  918   651 
1550                      party   party                  919   652 
1551                      party           ∅-2            919   None
1552                              party                  920   652 
1553               causelisten.   caus_                  921   653 
1554               causelisten.   list_n.                921   654 
1555                   Resp?nse   R_spons_               922   655 
1556                   Resp?nse           ∅-2            922   None
1557                              R_spons_               923   655 
1558       resp?nsibilityrep?rt   r_port                 924   657 
1559       resp?nsibilityrep?rt   r_sponsibility         924   656 
1560       resp?nsibilityrep?rt           ∅-2            924   None
1561                              r_port                 925   657 
1562                      music   music                  926   658 
1563            child.Payreveal           ∅-2            927   None
1564            child.Payreveal   child.Fr__             927   659 
1565                                      ∅-2            928   None
1566                      early           ∅-2            929   None
1567                matters?rt.           ∅-2            930   None
1568                      Eight           ∅-2            931   None
1569                       call           ∅-2            932   None
1570                   s?uthern           ∅-2            933   None
1571                    several           ∅-2            934   None
1572                                      ∅-2            935   None
1573                     expert           ∅-2            936   None
1574             kn?wledgefire.           ∅-2            937   None
1575             kn?wledgefire.   child.Fr__             937   659 
1576                              child.Fr__             938   659 
1577                        Any           ∅-2            939   None
1578                        Any   as                     939   660 
1579                 quicklyask           ∅-2            940   None
1580                                      ∅-2            941   None
1581                 key.Freeas           ∅-2            942   None
1582                 key.Freeas   as                     942   660 
1583                              as                     943   660 
1584                         d?   do                     944   661 
1585                 stati?n?ur   station                945   662 
1586                 stati?n?ur   our                    945   663 
1587                     apply.   apply.                 946   664 
1588                        Try   Try                    947   665 
1589                     dinner           ∅-2            948   None
1590                     dinner   dinn_r                 948   666 
1591                              dinn_r                 949   666 
1592             missi?n.Meth?d   mission.               950   667 
1593             missi?n.Meth?d   M_thod                 950   668 
1594                      under   und_r                  951   669 
1595                      st?re           ∅-2            952   None
1596                      st?re   stor_                  952   670 
1597                              stor_                  953   670 
1598                traditi?nal   traditional            954   671 
1599                 w?uldwith.   with.                  955   673 
1600                 w?uldwith.           ∅-2            955   None
1601                 w?uldwith.   would                  955   672 
1602                              with.                  956   673 
1603                    Pattern   Patt_rn                957   674 
1604             truthdirecti?n   dir_ction              958   676 
1605             truthdirecti?n   truth                  958   675 
1606                     p?lice   polic_                 959   677 
1607                     p?lice           ∅-2            959   None
1608                              polic_                 960   677 
1609                     recent   r_c_nt                 961   678 
1610                      plan.   plan.                  962   679 
1611                     Travel   Trav_l                 963   680 
1612                       yeah   y_ah                   964   681 
1613                       read   r_ad                   965   682 
1614                      l?cal   local                  966   683 
1615                     appear   app_ar                 967   684 
1616                 s?rt.Media   M_dia                  968   686 
1617                 s?rt.Media   sort.                  968   685 
1618                 s?rt.Media           ∅-2            968   None
1619                              M_dia                  969   686 
1620                h?mem?rning   hom_                   970   687 
1621                h?mem?rning   morning                970   688 
1622          bank.Particularly   bank.Particularly      971   689 
1623          bank.Particularly           ∅-2            971   None
1624                              bank.Particularly      972   689 
1625              studentresult   r_sult                 973   691 
1626              studentresult   stud_nt                973   690 
1627                      raise   rais_                  974   692 
1628                      raise           ∅-2            974   None
1629                              rais_                  975   692 
1630                 letterf?rm           ∅-2            976   None
1631                 letterf?rm   l_tt_r                 976   693 
1632                 letterf?rm   form                   976   694 
1633                              form                   977   694 
1634              v?ice.Science   voic_.                 978   695 
1635              v?ice.Science   Sci_nc_                978   696 
1636                       up?n   upon                   979   697 
1637                       nice   nic_                   980   698 
1638                       nice           ∅-2            980   None
1639                              nic_                   981   698 
1640                    present   pr_s_nt                982   699 
1641                livefeeling   liv_                   983   700 
1642                livefeeling   f__ling                983   701 
1643                livefeeling           ∅-2            983   None
1644                              f__ling                984   701 
1645                     claim.   claim.                 985   702 
1646                      Third   Third                  986   703 
1647                  rec?gnize   r_cogniz_              987   704 
1648                      wh?se   whos_                  988   705 
1649               hist?ry.Find           ∅-2            989   None
1650               hist?ry.Find   Find                   989   707 
1651               hist?ry.Find   history.               989   706 
1652                              Find                   990   707 
1653         dem?craticbuilding   building               991   709 
1654         dem?craticbuilding   d_mocratic             991   708 
1655         dem?craticbuilding           ∅-2            991   None
1656                              building               992   709 
1657                   daughter   daught_r               993   710 
1658               t?tala.Party   total                  994   711 
1659               t?tala.Party           ∅-2            994   None
1660                       back           ∅-2            995   None
1661                     f?rmer           ∅-2            996   None
1662                                      ∅-2            997   None
1663           perf?rmanceview.           ∅-2            998   None
1664                                      ∅-2            999   None
1665                       M?st           ∅-2           1000   None
1666                    finally           ∅-2           1001   None
1667                  s?metimes           ∅-2           1002   None
1668                realityunit           ∅-2           1003   None
1669                   pers?nal           ∅-2           1004   None
1670                    reas?n.           ∅-2           1005   None
1671                        Y?u           ∅-2           1006   None
1672                       skin           ∅-2           1007   None
1673                                      ∅-2           1008   None
1674                 designview           ∅-2           1009   None
1675                     bey?nd           ∅-2           1010   None
1676                                      ∅-2           1011   None
1677         wh?se.M?rninggr?up   total                 1012   711 
1678         wh?se.M?rninggr?up   group                 1012   713 
1679         wh?se.M?rninggr?up   a.Morning             1012   712 
1680         wh?se.M?rninggr?up           ∅-2           1012   None
1681                              group                 1013   713 
1682                      st?ck   stock                 1014   714 
1683                       kn?w   know                  1015   715 
1684                      pers?   p_r                   1016   716 
1685                      pers?   so                    1016   717 
1686                              so                    1017   717 
1687          C?ngress.Material   Mat_rial              1018   719 
1688          C?ngress.Material           ∅-2           1018   None
1689          C?ngress.Material   Congr_ss.             1018   718 
1690                              Mat_rial              1019   719 
1691                    imagine   imagin_               1020   720 
1692                s?ngth?ught   song                  1021   721 
1693                s?ngth?ught   thought               1021   722 
1694                        TV.   TV.                   1022   723 
1695                        TV.           ∅-2           1022   None
1696                              TV.                   1023   723 
1697                     Wh?arm   arm                   1024   725 
1698                     Wh?arm   Who                   1024   724 
1699                    f?reign   for_ign               1025   726 
1700             c?llecti?n.Old   coll_ction.Old        1026   727 
1701                     camera   cam_ra                1027   728 
1702                     t?ward           ∅-2           1028   None
1703                     t?ward   toward                1028   729 
1704                              toward                1029   729 
1705                 dataenergy   data                  1030   730 
1706                 dataenergy   _n_rgy                1030   731 
1707                     issue.           ∅-2           1031   None
1708                     issue.   issu_.                1031   732 
1709                              issu_.                1032   732 
1710                 Cardsystem   syst_m                1033   734 
1711                 Cardsystem   Card                  1033   733 
1712                       idea   id_a                  1034   735 
1713                       wish   wish                  1035   736 
1714                   pressure   pr_ssur_              1036   737 
1715                       wind   wind                  1037   738 
1716                              m__t                  1038   739 
1717                meeteffect.           ∅-2           1039   None
1718                meeteffect.   _ff_ct.               1039   740 
1719                meeteffect.   m__t                  1039   739 
1720                              _ff_ct.               1040   740 
1721                Changeall?w   Chang_                1041   741 
1722                Changeall?w   allow                 1041   742 
1723                       t?wn   town                  1042   743 
1724                       t?wn           ∅-2           1042   None
1725                              town                  1043   743 
1726              sistermanage.           ∅-2           1044   None
1727              sistermanage.   sist_r                1044   744 
1728              sistermanage.   manag_.               1044   745 
1729                              manag_.               1045   745 
1730                       M?st   Most                  1046   746 
1731              stateevery?ne   stat_                 1047   747 
1732              stateevery?ne   _v_ryon_              1047   748 
1733                     n?tice           ∅-2           1048   None
1734                     n?tice   notic_                1048   749 
1735                              notic_                1049   749 
1736       might.Military?thers   oth_rs                1050   751 
1737       might.Military?thers   might.Military        1050   750 
1738                        gun   gun                   1051   752 
1739                     th?ugh   though                1052   753 
1740                  p?litical   political             1053   754 
1741                  p?litical           ∅-2           1053   None
1742                              political             1054   754 
1743         internati?nalstar.   star.                 1055   756 
1744         internati?nalstar.   int_rnational         1055   755 
1745         internati?nalstar.           ∅-2           1055   None
1746                              star.                 1056   756 
1747                    T?pview   vi_w                  1057   758 
1748                    T?pview   Top                   1057   757 
1749                              go                    1058   759 
1750                      g?y?u   you                   1059   760 
1751                      g?y?u   go                    1059   759 
1752                     w?man.           ∅-2           1060   None
1753                     w?man.   woman.                1060   761 
1754                              woman.                1061   761 
1755                  Sc?redeal           ∅-2           1062   None
1756                  Sc?redeal   Scor_                 1062   762 
1757                  Sc?redeal   d_al                  1062   763 
1758                              d_al                  1063   763 
1759               b??kindicate   indicat_              1064   765 
1760               b??kindicate   book                  1064   764 
1761                  represent   r_pr_s_nt             1065   766 
1762                  represent           ∅-2           1065   None
1763                              r_pr_s_nt             1066   766 
1764               seat.C?untry   Country               1067   768 
1765               seat.C?untry   s_at.                 1067   767 
1766                       mean           ∅-2           1068   None
1767                       mean   m_an                  1068   769 
1768                              m_an                  1069   769 
1769                     simply   simply                1070   770 
1770                 finishfire   finish                1071   771 
1771                 finishfire   fir_                  1071   772 
1772                       n?t.           ∅-2           1072   None
1773                       n?t.   not.                  1072   773 
1774                              not.                  1073   773 
1775                    Seri?us   S_rious               1074   774 
1776                       game   gam_                  1075   775 
1777         bec?memean.With?ut   m_an.Pick             1076   777 
1778         bec?memean.With?ut   b_com_                1076   776 
1779         bec?memean.With?ut           ∅-2           1076   None
1780                       wish           ∅-2           1077   None
1781                      start           ∅-2           1078   None
1782                    certain           ∅-2           1079   None
1783                                      ∅-2           1080   None
1784                      learn           ∅-2           1081   None
1785                 kn?wthink.           ∅-2           1082   None
1786                      Teach           ∅-2           1083   None
1787                                      ∅-2           1084   None
1788                  finalvery           ∅-2           1085   None
1789                                      ∅-2           1086   None
1790                   audience           ∅-2           1087   None
1791                        ?ne           ∅-2           1088   None
1792                     green.           ∅-2           1089   None
1793                     Inside           ∅-2           1090   None
1794                  summerset           ∅-2           1091   None
1795                                      ∅-2           1092   None
1796              daughteradult           ∅-2           1093   None
1797               particularly           ∅-2           1094   None
1798                     ?ften.           ∅-2           1095   None
1799                                      ∅-2           1096   None
1800                   Reachget           ∅-2           1097   None
1801                        ?ne           ∅-2           1098   None
1802                     s?cial           ∅-2           1099   None
1803                  pr?fess?r           ∅-2           1100   None
1804                 dream.Pick   m_an.Pick             1101   777 
1805                 dream.Pick           ∅-2           1101   None
1806                              m_an.Pick             1102   777 
1807                     rec?rd   r_cord                1103   778 
1808               friendnature   fri_nd                1104   779 
1809               friendnature   natur_                1104   780 
1810                     lawyer   lawy_r                1105   781 
1811                     minute           ∅-2           1106   None
1812                     minute   minut_                1106   782 
1813                              minut_                1107   782 
1814                   br?ther.   broth_r.              1108   783 
1815                   Highals?   also                  1109   785 
1816                   Highals?   High                  1109   784 
1817                      p?wer           ∅-2           1110   None
1818                      p?wer   pow_r                 1110   786 
1819                              pow_r                 1111   786 
1820                     indeed   ind__d                1112   787 
1821                    evening   _v_ning               1113   788 
1822           summer.Different   Diff_r_nt             1114   790 
1823           summer.Different   summ_r.               1114   789 
1824                      wr?ng   wrong                 1115   791 
1825                      wr?ng           ∅-2           1115   None
1826                              wrong                 1116   791 
1827              leasttraining   training              1117   793 
1828              leasttraining   l_ast                 1117   792 
1829                                      ∅-2           1118   None
1830                   example.   _xampl_.              1119   794 
1831                   Whatever   What_v_r              1120   795 
1832               imageagainst   imag_                 1121   796 
1833               imageagainst   against               1121   797 
1834               imageagainst           ∅-2           1121   None
1835                              against               1122   797 
1836                        way   way                   1123   798 
1837       pull.Certainres?urce           ∅-2           1124   None
1838       pull.Certainres?urce   pull.Which            1124   799 
1839                        gun           ∅-2           1125   None
1840                      able.           ∅-2           1126   None
1841                       With           ∅-2           1127   None
1842                                      ∅-2           1128   None
1843                       size           ∅-2           1129   None
1844                      water           ∅-2           1130   None
1845                 pastappear           ∅-2           1131   None
1846                       pick           ∅-2           1132   None
1847                                      ∅-2           1133   None
1848                      s?uth           ∅-2           1134   None
1849                   PM.Which           ∅-2           1135   None
1850                   PM.Which   pull.Which            1135   799 
1851         individualtraining   training              1136   801 
1852         individualtraining   individual            1136   800 
1853                     any?ne   anyon_                1137   802 
1854                     speak.   sp_ak.                1138   803 
1855                       Once           ∅-2           1139   None
1856                       Once   Onc_                  1139   804 
1857                              Onc_                  1140   804 
1858            singletreatment           ∅-2           1141   None
1859            singletreatment   singl_                1141   805 
1860            singletreatment   tr_atm_nt             1141   806 
1861                              tr_atm_nt             1142   806 
1862                  actfriend   fri_nd                1143   808 
1863                  actfriend   act                   1143   807 
1864                    feeling   f__ling               1144   809 
1865                     think.   think.                1145   810 
1866                     think.           ∅-2           1145   None
1867                              think.                1146   810 
1868                Checkcareer   car__r                1147   812 
1869                Checkcareer   Ch_ck                 1147   811 
1870                      maybe   mayb_                 1148   813 
1871                       side   sid_                  1149   814 
1872                  security.   s_curity.             1150   815 
1873                        Any   Any                   1151   816 
1874                        Any           ∅-2           1151   None
1875                              Any                   1152   816 
1876                p?pularl?ng   long                  1153   818 
1877                p?pularl?ng           ∅-2           1153   None
1878                p?pularl?ng   popular               1153   817 
1879                              long                  1154   818 
1880                     sh?uld   should                1155   819 
1881                   y?ual?ne   alon_                 1156   821 
1882                   y?ual?ne   you                   1156   820 
1883                   y?ual?ne           ∅-2           1156   None
1884                              alon_                 1157   821 
1885                   strategy   strat_gy              1158   822 
1886             fact.Challenge   fact.Incr_as_         1159   823 
1887             fact.Challenge           ∅-2           1159   None
1888                 greenwrite           ∅-2           1160   None
1889                        ?ld           ∅-2           1161   None
1890                    br?ther           ∅-2           1162   None
1891                                      ∅-2           1163   None
1892               thr?w.W?rker           ∅-2           1164   None
1893                                      ∅-2           1165   None
1894                   maj?rity           ∅-2           1166   None
1895                 trialtruth           ∅-2           1167   None
1896                   message.           ∅-2           1168   None
1897                                      ∅-2           1169   None
1898                       Hard           ∅-2           1170   None
1899                       east           ∅-2           1171   None
1900                  wideh?tel           ∅-2           1172   None
1901                     ph?ne.           ∅-2           1173   None
1902                                      ∅-2           1174   None
1903               W?rkerdetail           ∅-2           1175   None
1904                                      ∅-2           1176   None
1905                  dealcivil           ∅-2           1177   None
1906                                      ∅-2           1178   None
1907                c?nsumerrun           ∅-2           1179   None
1908                   certain.           ∅-2           1180   None
1909                        But           ∅-2           1181   None
1910                     w?rker           ∅-2           1182   None
1911                                      ∅-2           1183   None
1912             imaginesuccess           ∅-2           1184   None
1913                        y?u           ∅-2           1185   None
1914                                      ∅-2           1186   None
1915       back.Increasereceive   fact.Incr_as_         1187   823 
1916       back.Increasereceive           ∅-2           1187   None
1917       back.Increasereceive   r_c_iv_               1187   824 
1918                        f?r   for                   1188   825 
1919                      event   _v_nt                 1189   826 
1920                      s?me.           ∅-2           1190   None
1921                      s?me.   som_.                 1190   827 
1922                              som_.                 1191   827 
1923                Treatmember           ∅-2           1192   None
1924                Treatmember   Tr_at                 1192   828 
1925                Treatmember   m_mb_r                1192   829 
1926                              m_mb_r                1193   829 
1927                   building   building              1194   830 
1928          s?cietymanagement   manag_m_nt            1195   832 
1929          s?cietymanagement   soci_ty               1195   831 
1930          s?cietymanagement           ∅-2           1195   None
1931                              manag_m_nt            1196   832 
1932                       fly.   fly.                  1197   833 
1933               Differenceas   as                    1198   835 
1934               Differenceas   Diff_r_nc_            1198   834 
1935                              as                    1199   835 
1936                    b?dyhis   his                   1200   837 
1937                    b?dyhis   body                  1200   836 
1938                    either.   _ith_r.               1201   838 
1939                    either.           ∅-2           1201   None
1940                              _ith_r.               1202   838 
1941                       Wind   Wind                  1203   839 
1942        administrati?ndrive   administration        1204   840 
1943        administrati?ndrive   driv_                 1204   841 
1944                        ?ur           ∅-2           1205   None
1945                        ?ur   our                   1205   842 
1946                              our                   1206   842 
1947                 s?und.Free   sound.Fr__            1207   843 
1948                  treatment   tr_atm_nt             1208   844 
1949         resp?nsibilitymuch   r_sponsibility        1209   845 
1950         resp?nsibilitymuch           ∅-2           1209   None
1951         resp?nsibilitymuch   much                  1209   846 
1952                              much                  1210   846 
1953             f?rgetDem?crat   forg_t                1211   847 
1954             f?rgetDem?crat   D_mocrat              1211   848 
1955                    leader.   l_ad_r.               1212   849 
1956                    leader.           ∅-2           1212   None
1957                              l_ad_r.               1213   849 
1958               Benefitserve   B_n_fit               1214   850 
1959               Benefitserve   s_rv_                 1214   851 
1960                    perhaps   p_rhaps               1215   852 
1961                       s?ng   song                  1216   853 
1962                  behavi?r.   b_havior.             1217   854 
1963                  behavi?r.           ∅-2           1217   None
1964                              b_havior.             1218   854 
1965                       Kn?w   Know                  1219   855 
1966                       hand   hand                  1220   856 
1967         C?ngressunder.Part           ∅-2           1221   None
1968         C?ngressunder.Part   und_r.Part            1221   858 
1969         C?ngressunder.Part   Congr_ss              1221   857 
1970                              und_r.Part            1222   858 
1971               languagesame   languag_              1223   859 
1972               languagesame   sam_                  1223   860 
1973                              sam_                  1224   860 
1974                whichrep?rt           ∅-2           1225   None
1975                whichrep?rt   which                 1225   861 
1976                whichrep?rt   r_port                1225   862 
1977                              r_port                1226   862 
1978              t?wn.Pr?bably           ∅-2           1227   None
1979              t?wn.Pr?bably   town.                 1227   863 
1980              t?wn.Pr?bably   Probably              1227   864 
1981                              Probably              1228   864 
1982                      carry   carry                 1229   865 
1983                  partyseek   s__k                  1230   867 
1984                  partyseek   party                 1230   866 
1985                              s__k                  1231   867 
1986                     during   during                1232   868 
1987                    effect.   _ff_ct.               1233   869 
1988                Suggestpush   push                  1234   871 
1989                Suggestpush           ∅-2           1234   None
1990                Suggestpush   Sugg_st               1234   870 
1991                              push                  1235   871 
1992                   meeting.   m__ting.              1236   872 
1993               Pr?pertyh?me   Prop_rty              1237   873 
1994               Pr?pertyh?me   hom_                  1237   874 
1995                      m?del           ∅-2           1238   None
1996                      m?del   mod_l                 1238   875 
1997                              mod_l                 1239   875 
1998                        be.   b_.                   1240   876 
1999                       Once   Onc_                  1241   877 
2000            participantwind   wind                  1242   879 
2001            participantwind   participant           1242   878 
2002            participantwind           ∅-2           1242   None
2003                              wind                  1243   879 
2004               increasewind           ∅-2           1244   None
2005               increasewind   incr_as_              1244   880 
2006               increasewind   wind                  1244   881 
2007                              wind                  1245   881 
2008                 late.Music           ∅-2           1246   None
2009                 late.Music   lat_.R_duc_           1246   882 
2010               culturalup?n           ∅-2           1247   None
2011                        n?r           ∅-2           1248   None
2012                     st?ry.           ∅-2           1249   None
2013                  Interview           ∅-2           1250   None
2014                                      ∅-2           1251   None
2015                   Dem?crat           ∅-2           1252   None
2016              healtheff?rt.           ∅-2           1253   None
2017                      V?ice           ∅-2           1254   None
2018                                      ∅-2           1255   None
2019                   atmatter           ∅-2           1256   None
2020                                      ∅-2           1257   None
2021                    indeed.           ∅-2           1258   None
2022             Weightc?nsumer           ∅-2           1259   None
2023                                      ∅-2           1260   None
2024                      table           ∅-2           1261   None
2025                religi?usas           ∅-2           1262   None
2026                                      ∅-2           1263   None
2027                        Mr.           ∅-2           1264   None
2028                        Gun           ∅-2           1265   None
2029                      l?cal           ∅-2           1266   None
2030                     bestt?           ∅-2           1267   None
2031              bec?me.Reduce   lat_.R_duc_           1268   882 
2032              bec?me.Reduce           ∅-2           1268   None
2033                 investment   inv_stm_nt            1269   883 
2034                         g?   go                    1270   884 
2035                         g?           ∅-2           1270   None
2036                              go                    1271   884 
2037            difficultfriend   difficult             1272   885 
2038            difficultfriend   fri_nd                1272   886 
2039            difficultfriend           ∅-2           1272   None
2040                              fri_nd                1273   886 
2041                 clearly.Pm   Pm                    1274   888 
2042                 clearly.Pm           ∅-2           1274   None
2043                 clearly.Pm   cl_arly.              1274   887 
2044                              Pm                    1275   888 
2045                        h?w   how                   1276   889 
2046                     spring   spring                1277   890 
2047                    darkgun   dark                  1278   891 
2048                    darkgun   gun                   1278   892 
2049                    expert.           ∅-2           1279   None
2050                    expert.   _xp_rt.               1279   893 
2051                              _xp_rt.               1280   893 
2052                     Opti?n   Option                1281   894 
2053                    whether   wh_th_r               1282   895 
2054                eyephysical   _y_                   1283   896 
2055                eyephysical   physical              1283   897 
2056                       step   st_p                  1284   898 
2057                     matter   matt_r                1285   899 
2058                     matter           ∅-2           1285   None
2059                              matt_r                1286   899 
2060                 ahead.Wind   ah_ad.                1287   900 
2061                 ahead.Wind   Wind                  1287   901 
2062                    medical           ∅-2           1288   None
2063                    medical   m_dical               1288   902 
2064                              m_dical               1289   902 
2065                        tax   tax                   1290   903 
2066                    special   sp_cial               1291   904 
2067                  f??tball.   ball.                 1292   906 
2068                  f??tball.           ∅-2           1292   None
2069                  f??tball.   foot                  1292   905 
2070                              ball.                 1293   906 
2071               T?dayinstead   inst_ad               1294   908 
2072               T?dayinstead   Today                 1294   907 
2073                 c?nference   conf_r_nc_            1295   909 
2074                 c?nference           ∅-2           1295   None
2075                              conf_r_nc_            1296   909 
2076               whether.Time   wh_th_r.Tim_          1297   910 
2077               despitequite   quit_                 1298   912 
2078               despitequite   d_spit_               1298   911 
2079               despitequite           ∅-2           1298   None
2080                              quit_                 1299   912 
2081                       skin   skin                  1300   913 
2082          anythinganything.   anything.             1301   915 
2083          anythinganything.   anything              1301   914 
2084          anythinganything.           ∅-2           1301   None
2085                              anything.             1302   915 
2086                   Fallm?re   Fall                  1303   916 
2087                   Fallm?re   mor_                  1303   917 
2088                       face           ∅-2           1304   None
2089                       face   fac_                  1304   918 
2090                              fac_                  1305   918 
2091                 yesc?ncern   y_s                   1306   919 
2092                 yesc?ncern   conc_rn               1306   920 
2093                 yesc?ncern           ∅-2           1306   None
2094                              conc_rn               1307   920 
2095              ranges?me?ne.   som_on_.              1308   922 
2096              ranges?me?ne.   rang_                 1308   921 
2097              ranges?me?ne.           ∅-2           1308   None
2098                              som_on_.              1309   922 
2099                  Kn?wledge   Knowl_dg_             1310   923 
2100              severaldecide   s_v_ral               1311   924 
2101              severaldecide           ∅-2           1311   None
2102              severaldecide   d_cid_                1311   925 
2103                              d_cid_                1312   925 
2104                       need   n__d                  1313   926 
2105                        eat   _at                   1314   927 
2106   nati?nal.An?theralth?ugh   national.It_m         1315   928 
2107   nati?nal.An?theralth?ugh           ∅-2           1315   None
2108                                      ∅-2           1316   None
2109          traditi?nalassume           ∅-2           1317   None
2110                  c?nsider.           ∅-2           1318   None
2111                      Skill           ∅-2           1319   None
2112                                      ∅-2           1320   None
2113                     manage           ∅-2           1321   None
2114                  viewbank.           ∅-2           1322   None
2115                     The?ry           ∅-2           1323   None
2116                       free           ∅-2           1324   None
2117                   natural.           ∅-2           1325   None
2118                                      ∅-2           1326   None
2119                       Pick           ∅-2           1327   None
2120                traditi?nal           ∅-2           1328   None
2121                     series           ∅-2           1329   None
2122                     debate           ∅-2           1330   None
2123                      agent           ∅-2           1331   None
2124                    reveal.           ∅-2           1332   None
2125                      While           ∅-2           1333   None
2126              f?rcegeneral.           ∅-2           1334   None
2127                        Lay           ∅-2           1335   None
2128                                      ∅-2           1336   None
2129                      tw?d?           ∅-2           1337   None
2130                                      ∅-2           1338   None
2131                       hard           ∅-2           1339   None
2132                  haveth?se           ∅-2           1340   None
2133                  rule.Item           ∅-2           1341   None
2134                  rule.Item   national.It_m         1341   928 
2135                       easy           ∅-2           1342   None
2136                       easy   _asy                  1342   929 
2137                              _asy                  1343   929 
2138            clearlycampaign   cl_arly               1344   930 
2139            clearlycampaign   campaign              1344   931 
2140                       will   will                  1345   932 
2141                    either.   _ith_r.               1346   933 
2142                   Security   S_curity              1347   934 
2143                        yet   y_t                   1348   935 
2144                        yet           ∅-2           1348   None
2145                              y_t                   1349   935 
2146                      crime   crim_                 1350   936 
2147               scientistwin   win                   1351   938 
2148               scientistwin   sci_ntist             1351   937 
2149                     ?pti?n           ∅-2           1352   None
2150                     ?pti?n   option                1352   939 
2151                              option                1353   939 
2152                       l?t.   lot.                  1354   940 
2153             Fiveeverything   Fiv_                  1355   941 
2154             Fiveeverything   _v_rything            1355   942 
2155                    similar   similar               1356   943 
2156                   reality.   r_ality.              1357   944 
2157                   reality.           ∅-2           1357   None
2158                              r_ality.              1358   944 
2159                     Player   Play_r                1359   945 
2160                 winddecide   d_cid_                1360   947 
2161                 winddecide           ∅-2           1360   None
2162                 winddecide   wind                  1360   946 
2163                              d_cid_                1361   947 
2164                        she   sh_                   1362   948 
2165                  c?ntinue.   continu_.             1363   949 
2166                     Cupshe   Cup                   1364   950 
2167                     Cupshe   sh_                   1364   951 
2168                              sh_                   1365   951 
2169                     energy   _n_rgy                1366   952 
2170                       miss   miss                  1367   953 
2171                c?ursestill   still                 1368   955 
2172                c?ursestill   cours_                1368   954 
2173                c?ursestill           ∅-2           1368   None
2174                              still                 1369   955 
2175               res?urce.Act           ∅-2           1370   None
2176               res?urce.Act   r_sourc_.Just         1370   956 
2177                  candidate           ∅-2           1371   None
2178                  suchsh?rt           ∅-2           1372   None
2179                       half           ∅-2           1373   None
2180                                      ∅-2           1374   None
2181                  rulechair           ∅-2           1375   None
2182                    ?ffice.           ∅-2           1376   None
2183                      Radi?           ∅-2           1377   None
2184                         we           ∅-2           1378   None
2185                                      ∅-2           1379   None
2186                    th?ught           ∅-2           1380   None
2187                      start           ∅-2           1381   None
2188                       play           ∅-2           1382   None
2189                         PM           ∅-2           1383   None
2190                     s?und.           ∅-2           1384   None
2191                       Task           ∅-2           1385   None
2192                      agree           ∅-2           1386   None
2193                leaderadmit           ∅-2           1387   None
2194                   reflect.           ∅-2           1388   None
2195                   Material           ∅-2           1389   None
2196                      ahead           ∅-2           1390   None
2197                                      ∅-2           1391   None
2198         decisi?nh?me.Maybe           ∅-2           1392   None
2199                       deal           ∅-2           1393   None
2200                       r?le           ∅-2           1394   None
2201                  educati?n           ∅-2           1395   None
2202                         at           ∅-2           1396   None
2203                       face           ∅-2           1397   None
2204                     radi?.           ∅-2           1398   None
2205                 Especially           ∅-2           1399   None
2206                                      ∅-2           1400   None
2207                 ?fferst?re           ∅-2           1401   None
2208                                      ∅-2           1402   None
2209                  myselfnew           ∅-2           1403   None
2210                                      ∅-2           1404   None
2211               maj?rityman.           ∅-2           1405   None
2212                                      ∅-2           1406   None
2213                    Pr?duce           ∅-2           1407   None
2214           m?vementC?ngress           ∅-2           1408   None
2215                                      ∅-2           1409   None
2216         maybe?fficial.Just           ∅-2           1410   None
2217         maybe?fficial.Just   r_sourc_.Just         1410   956 
2218                    already           ∅-2           1411   None
2219                    already   alr_ady               1411   957 
2220                              alr_ady               1412   957 
2221                      treat   tr_at                 1413   958 
2222                  s?uthern.   south_rn.             1414   959 
2223                     B?thup   up                    1415   961 
2224                     B?thup   Both                  1415   960 
2225                      media   m_dia                 1416   962 
2226                      w?man   woman                 1417   963 
2227                                      ∅-2           1418   None
2228                      enj?y   _njoy                 1419   964 
2229                    ?kneed.   n__d.                 1420   966 
2230                    ?kneed.   ok                    1420   965 
2231                       Well   W_ll                  1421   967 
2232                       wide           ∅-2           1422   None
2233                       wide   wid_                  1422   968 
2234                              wid_                  1423   968 
2235                     health   h_alth                1424   969 
2236                landthr?ugh   through               1425   971 
2237                landthr?ugh   land                  1425   970 
2238                landthr?ugh           ∅-2           1425   None
2239                              through               1426   971 
2240                       west   w_st                  1427   972 
2241       hundred.Relati?nship   hundr_d.              1428   973 
2242       hundred.Relati?nship   R_lationship          1428   974 
2243                       east   _ast                  1429   975 
2244                    c?ntr?l   control               1430   976 
2245                     wind?w   window                1431   977 
2246                    c?ncern   conc_rn               1432   978 
2247                chance.Mind   chanc_.Mind           1433   979 
2248                    impr?ve   improv_               1434   980 
2249                       main   main                  1435   981 
2250                        t??   too                   1436   982 
2251                      v?ice           ∅-2           1437   None
2252                      v?ice   voic_                 1437   983 
2253                              voic_                 1438   983 
2254                   manager.   manag_r.              1439   984 
2255                 N?rf?rward   forward               1440   986 
2256                 N?rf?rward   Nor                   1440   985 
2257                       seek   s__k                  1441   987 
2258                       seek           ∅-2           1441   None
2259                              s__k                  1442   987 
2260                        gun   gun                   1443   988 
2261                       save   sav_                  1444   989 
2262              planspecific.   plan                  1445   990 
2263              planspecific.   sp_cific.             1445   991 
2264                       Will           ∅-2           1446   None
2265                       Will   Will                  1446   992 
2266                              Will                  1447   992 
2267                  veryseven   s_v_n                 1448   994 
2268                  veryseven   v_ry                  1448   993 
2269                  veryseven           ∅-2           1448   None
2270                              s_v_n                 1449   994 
2271                      life.   lif_.                 1450   995 
2272             Cust?mermyself   mys_lf                1451   997 
2273             Cust?mermyself   Custom_r              1451   996 
2274             Cust?mermyself           ∅-2           1451   None
2275                              mys_lf                1452   997 
2276                   research   r_s_arch              1453   998 
2277                      m?st.   most.                 1454   999 
2278           Priceperf?rmance           ∅-2           1455   None
2279           Priceperf?rmance   p_rformanc_           1455   1001
2280           Priceperf?rmance   Pric_                 1455   1000
2281                              p_rformanc_           1456   1001
2282               nearstart.N?           ∅-2           1457   None
2283               nearstart.N?   n_ar                  1457   1002
2284               nearstart.N?   start.No              1457   1003
2285                              start.No              1458   1003
2286                   therepay           ∅-2           1459   None
2287                   therepay   th_r_                 1459   1004
2288                   therepay   pay                   1459   1005
2289                              pay                   1460   1005
2290                     p?wer.   pow_r.                1461   1006
2291                     Shesay   say                   1462   1008
2292                     Shesay   Sh_                   1462   1007
2293                     Shesay           ∅-2           1462   None
2294                              say                   1463   1008
2295                     accept   acc_pt                1464   1009
2296              ?pti?nsimply.   option                1465   1010
2297              ?pti?nsimply.   simply.               1465   1011
2298                       Up?n   Upon                  1466   1012
2299                     th?ugh   though                1467   1013
2300                    prevent   pr_v_nt               1468   1014
2301                       ?ver           ∅-2           1469   None
2302                       ?ver   ov_r                  1469   1015
2303                              ov_r                  1470   1015
2304             underpresident   und_r                 1471   1016
2305             underpresident           ∅-2           1471   None
2306             underpresident   pr_sid_nt             1471   1017
2307                              pr_sid_nt             1472   1017
2308                       dark   dark                  1473   1018
2309            citizen.Acc?unt   Account               1474   1020
2310            citizen.Acc?unt   citiz_n.              1474   1019
2311                       y?ur   your                  1475   1021
2312                      clear   cl_ar                 1476   1022
2313                      clear           ∅-2           1476   None
2314                              cl_ar                 1477   1022
2315              researchthr?w   r_s_arch              1478   1023
2316              researchthr?w   throw                 1478   1024
2317                      trade   trad_                 1479   1025
2318                     budget   budg_t                1480   1026
2319                     budget           ∅-2           1480   None
2320                              budg_t                1481   1026
2321         child.Rememberrace   rac_                  1482   1028
2322         child.Rememberrace   child.R_m_mb_r        1482   1027
2323                       team   t_am                  1483   1029
2324                       team           ∅-2           1483   None
2325                              t_am                  1484   1029
2326                       line   lin_                  1485   1030
2327                      fr?nt   front                 1486   1031
2328                   evidence   _vid_nc_              1487   1032
2329                    herself   h_rs_lf               1488   1033
2330                   p?pular.   popular.              1489   1034
2331                      Reach   R_ach                 1490   1035
2332                    exactly   _xactly               1491   1036
2333                 tend?pti?n           ∅-2           1492   None
2334                 tend?pti?n   t_nd                  1492   1037
2335                 tend?pti?n   option                1492   1038
2336                              option                1493   1038
2337                       wait   wait                  1494   1039
2338                  security.   s_curity.             1495   1040
2339                       Past   Past                  1496   1041
2340                  pickw?rld   world                 1497   1043
2341                  pickw?rld   pick                  1497   1042
2342                  pickw?rld           ∅-2           1497   None
2343                              world                 1498   1043
2344          gasrecent.Machine           ∅-2           1499   None
2345          gasrecent.Machine   gas                   1499   1044
2346          gasrecent.Machine   r_c_nt.Machin_        1499   1045
2347                              r_c_nt.Machin_        1500   1045
2348                trueacc?unt           ∅-2           1501   None
2349                trueacc?unt   tru_                  1501   1046
2350                trueacc?unt   account               1501   1047
2351                              account               1502   1047
2352                    tr?uble   troubl_               1503   1048
2353                    culture   cultur_               1504   1049
2354                     ?ccur.   occur.                1505   1050
2355             Watercharacter   charact_r             1506   1052
2356             Watercharacter   Wat_r                 1506   1051
2357                        sea   s_a                   1507   1053
2358                    bef?re.           ∅-2           1508   None
2359                    bef?re.   b_for_.               1508   1054
2360                              b_for_.               1509   1054
2361            Specificmanager   Sp_cific              1510   1055
2362            Specificmanager           ∅-2           1510   None
2363            Specificmanager   manag_r               1510   1056
2364                              manag_r               1511   1056
2365                 thisthreat   thr_at                1512   1058
2366                 thisthreat   this                  1512   1057
2367                       f??d   food                  1513   1059
2368                        bed   b_d                   1514   1060
2369                        bed           ∅-2           1514   None
2370                              b_d                   1515   1060
2371                      r?ck.   rock.                 1516   1061
2372                 Fastp?licy   Fast                  1517   1062
2373                 Fastp?licy   policy                1517   1063
2374                       that   that                  1518   1064
2375                     public   public                1519   1065
2376                     public           ∅-2           1519   None
2377                              public                1520   1065
2378                    usually   usually               1521   1066
2379                      small   small                 1522   1067
2380       sh?ulderc?ver.Happen   cov_r.Happ_n          1523   1069
2381       sh?ulderc?ver.Happen   should_r              1523   1068
2382                    between           ∅-2           1524   None
2383                    between   b_tw__n               1524   1070
2384                              b_tw__n               1525   1070
2385              thenc?mputer.   th_n                  1526   1071
2386              thenc?mputer.   comput_r.             1526   1072
2387                      Y?ung   Young                 1527   1073
2388                      Y?ung           ∅-2           1527   None
2389                              Young                 1528   1073
2390                       site   sit_                  1529   1074
2391                       d?wn   down                  1530   1075
2392                    ifexist   if                    1531   1076
2393                    ifexist   _xist                 1531   1077
2394                    resp?nd   r_spond               1532   1078
2395                     artist           ∅-2           1533   None
2396                     artist   artist                1533   1079
2397                              artist                1534   1079
2398               church.Enter           ∅-2           1535   None
2399               church.Enter   Ent_r                 1535   1081
2400               church.Enter   church.               1535   1080
2401                              Ent_r                 1536   1081
2402         resp?nsibilitythan   than                  1537   1083
2403         resp?nsibilitythan           ∅-2           1537   None
2404         resp?nsibilitythan   r_sponsibility        1537   1082
2405                              than                  1538   1083
2406                      f?ur.   four.                 1539   1084
2407                Remainvisit   visit                 1540   1086
2408                Remainvisit   R_main                1540   1085
2409                Remainvisit           ∅-2           1540   None
2410                              visit                 1541   1086
2411               reflectpeace   p_ac_                 1542   1088
2412               reflectpeace           ∅-2           1542   None
2413               reflectpeace   r_fl_ct               1542   1087
2414                              p_ac_                 1543   1088
2415                    benefit   b_n_fit               1544   1089
2416             n?thing.Chance   nothing.Chanc_        1545   1090
2417                    quickly   quickly               1546   1091
2418                   yesglass   glass                 1547   1093
2419                   yesglass   y_s                   1547   1092
2420                     pe?ple   p_opl_                1548   1094
2421                      st?ck   stock                 1549   1095
2422                      seek.   s__k.                 1550   1096
2423                      Argue   Argu_                 1551   1097
2424                      Argue           ∅-2           1551   None
2425                              Argu_                 1552   1097
2426             eff?rtwhatever   _ffort                1553   1098
2427             eff?rtwhatever           ∅-2           1553   None
2428             eff?rtwhatever   what_v_r              1553   1099
2429                              what_v_r              1554   1099
2430                      where   wh_r_                 1555   1100
2431                    prepare   pr_par_               1556   1101
2432                    little.   littl_.               1557   1102
2433                    Meeting   M__ting               1558   1103
2434               imagineab?ut   imagin_               1559   1104
2435               imagineab?ut   about                 1559   1105
2436                       with   with                  1560   1106
2437                       with           ∅-2           1560   None
2438                              with                  1561   1106
2439        stand.Pr?tectdesign   stand.Prot_ct         1562   1107
2440        stand.Pr?tectdesign   d_sign                1562   1108
2441                    manager   manag_r               1563   1109
2442                       sing   sing                  1564   1110
2443                       sing           ∅-2           1564   None
2444                              sing                  1565   1110
2445          culturalrecently.           ∅-2           1566   None
2446          culturalrecently.   r_c_ntly.             1566   1112
2447          culturalrecently.   cultural              1566   1111
2448                              r_c_ntly.             1567   1112
2449               F?reignal?ne   alon_                 1568   1114
2450               F?reignal?ne   For_ign               1568   1113
2451                       sing   sing                  1569   1115
2452                       b?dy   body                  1570   1116
2453                     really   r_ally                1571   1117
2454                  campaign.   campaign.             1572   1118
2455                      Fight   Fight                 1573   1119
2456                      Fight           ∅-2           1573   None
2457                              Fight                 1574   1119
2458                       make   mak_                  1575   1120
2459                     anywin   any                   1576   1121
2460                     anywin           ∅-2           1576   None
2461                     anywin   win                   1576   1122
2462                              win                   1577   1122
2463                     bef?re   b_for_                1578   1123
2464                animal.Well   animal.W_ll           1579   1124
2465                  handcarry   hand                  1580   1125
2466                  handcarry   carry                 1580   1126
2467                  handcarry           ∅-2           1580   None
2468                              carry                 1581   1126
2469                     plant.   plant.                1582   1127
2470                      Dream   Dr_am                 1583   1128
2471            questi?nbelieve   b_li_v_               1584   1130
2472            questi?nbelieve   qu_stion              1584   1129
2473                      c?uld   could                 1585   1131
2474                     family   family                1586   1132
2475                      admit   admit                 1587   1133
2476                        new   n_w                   1588   1134
2477                    seas?n.   s_ason.               1589   1135
2478                    Finally   Finally               1590   1136
2479                        can   can                   1591   1137
2480                                      ∅-2           1592   None
2481            eveningc?nsumer   _v_ning               1593   1138
2482            eveningc?nsumer   consum_r              1593   1139
2483            eveningc?nsumer           ∅-2           1593   None
2484                              consum_r              1594   1139
2485                       sign   sign                  1595   1140
2486                pr?vepers?n   p_rson                1596   1142
2487                pr?vepers?n   prov_                 1596   1141
2488                pr?vepers?n           ∅-2           1596   None
2489                              p_rson                1597   1142
2490        buy.F?rgetdifferent   buy.Forg_t            1598   1143
2491        buy.F?rgetdifferent   diff_r_nt             1598   1144
2492                                      ∅-2           1599   None
2493            everyb?dystuff.   stuff.                1600   1146
2494            everyb?dystuff.           ∅-2           1600   None
2495            everyb?dystuff.   _v_rybody             1600   1145
2496                              stuff.                1601   1146
2497                    Evening   Ev_ning               1602   1147
2498                  s?uthidea   id_a                  1603   1149
2499                  s?uthidea   south                 1603   1148
2500                        eye   _y_                   1604   1150
2501                        eye           ∅-2           1604   None
2502                              _y_                   1605   1150
2503                     if.Get   G_t                   1606   1152
2504                     if.Get           ∅-2           1606   None
2505                     if.Get   if.                   1606   1151
2506                              G_t                   1607   1152
2507                    with?ut   without               1608   1153
2508                 springlast   spring                1609   1154
2509                 springlast           ∅-2           1609   None
2510                 springlast   last                  1609   1155
2511                              last                  1610   1155
2512                       c?ld   cold                  1611   1156
2513                   few.That   That                  1612   1158
2514                   few.That   f_w.                  1612   1157
2515                      black   black                 1613   1159
2516                      black           ∅-2           1613   None
2517                              black                 1614   1159
2518                        sit   sit                   1615   1160
2519                     accept   acc_pt                1616   1161
2520                       main   main                  1617   1162
2521                       wife   wif_                  1618   1163
2522              eachp?siti?n.   _ach                  1619   1164
2523              eachp?siti?n.   position.             1619   1165
2524                     Expert   Exp_rt                1620   1166
2525                      av?id           ∅-2           1621   None
2526                      av?id   avoid                 1621   1167
2527                              avoid                 1622   1167
2528              acr?ssf?reign   across                1623   1168
2529              acr?ssf?reign   for_ign               1623   1169
2530                 t?p.Speech           ∅-2           1624   None
2531                 t?p.Speech   top.Indicat_          1624   1170
2532                                      ∅-2           1625   None
2533                 generati?n           ∅-2           1626   None
2534               suggestskill           ∅-2           1627   None
2535                                      ∅-2           1628   None
2536                 base.Y?ung           ∅-2           1629   None
2537                                      ∅-2           1630   None
2538                      speak           ∅-2           1631   None
2539                 m?uthtalk.           ∅-2           1632   None
2540                                      ∅-2           1633   None
2541                    Yetcare           ∅-2           1634   None
2542                                      ∅-2           1635   None
2543                      under           ∅-2           1636   None
2544                  increase.           ∅-2           1637   None
2545                       Feel           ∅-2           1638   None
2546                    yesf??t           ∅-2           1639   None
2547                     en?ugh           ∅-2           1640   None
2548                                      ∅-2           1641   None
2549                 d?.Reality           ∅-2           1642   None
2550                  sidem?nth           ∅-2           1643   None
2551                       fall           ∅-2           1644   None
2552                                      ∅-2           1645   None
2553                      just.           ∅-2           1646   None
2554              Serve?fficial           ∅-2           1647   None
2555                                      ∅-2           1648   None
2556                  finalstay           ∅-2           1649   None
2557                                      ∅-2           1650   None
2558               testc?mpany.           ∅-2           1651   None
2559                                      ∅-2           1652   None
2560                     Simple           ∅-2           1653   None
2561          presentp?pulati?n           ∅-2           1654   None
2562                   kitchen.           ∅-2           1655   None
2563                    An?ther           ∅-2           1656   None
2564                       nice           ∅-2           1657   None
2565                    vari?us           ∅-2           1658   None
2566                                      ∅-2           1659   None
2567                  freefact.           ∅-2           1660   None
2568                     Am?unt           ∅-2           1661   None
2569                                      ∅-2           1662   None
2570                   att?rney           ∅-2           1663   None
2571                  safejust.           ∅-2           1664   None
2572                       Skin           ∅-2           1665   None
2573                                      ∅-2           1666   None
2574              l?tg?vernment           ∅-2           1667   None
2575                     ch?ice           ∅-2           1668   None
2576                                      ∅-2           1669   None
2577              full.Indicate           ∅-2           1670   None
2578              full.Indicate   top.Indicat_          1670   1170
2579                         TV   TV                    1671   1171
2580            s?cietyn?thing.           ∅-2           1672   None
2581            s?cietyn?thing.   soci_ty               1672   1172
2582            s?cietyn?thing.   nothing.              1672   1173
2583                              nothing.              1673   1173
2584                  All?wrise   ris_                  1674   1175
2585                  All?wrise   Allow                 1674   1174
2586                        pay   pay                   1675   1176
2587                      c?ach   coach                 1676   1177
2588                  res?urce.   r_sourc_.             1677   1178
2589                  res?urce.           ∅-2           1677   None
2590                              r_sourc_.             1678   1178
2591         Standardexperience   _xp_ri_nc_            1679   1180
2592         Standardexperience   Standard              1679   1179
2593         Standardexperience           ∅-2           1679   None
2594                              _xp_ri_nc_            1680   1180
2595                  rec?gnize   r_cogniz_             1681   1181
2596           beautifularrive.   b_autiful             1682   1182
2597           beautifularrive.   arriv_.               1682   1183
2598           beautifularrive.           ∅-2           1682   None
2599                              arriv_.               1683   1183
2600                  Executive   Ex_cutiv_             1684   1184
2601                      ahead   ah_ad                 1685   1185
2602                     c?ach.   coach.                1686   1186
2603                     Friend   Fri_nd                1687   1187
2604                  v?iced?wn   down                  1688   1189
2605                  v?iced?wn   voic_                 1688   1188
2606                      chair           ∅-2           1689   None
2607                      chair   chair                 1689   1190
2608                              chair                 1690   1190
2609          menti?neverything   m_ntion               1691   1191
2610          menti?neverything   _v_rything            1691   1192
2611            bey?nd.Cust?mer   b_yond.Custom_r       1692   1193
2612                     ch?ice   choic_                1693   1194
2613                     ch?ice           ∅-2           1693   None
2614                              choic_                1694   1194
2615             milli?nc?mpany   company               1695   1196
2616             milli?nc?mpany   million               1695   1195
2617                     during   during                1696   1197
2618                       f??t   foot                  1697   1198
2619                       face           ∅-2           1698   None
2620                       face   fac_                  1698   1199
2621                              fac_                  1699   1199
2622                 study.Fr?m   From                  1700   1201
2623                 study.Fr?m   study.                1700   1200
2624                       yard   yard                  1701   1202
2625                      trial           ∅-2           1702   None
2626                      trial   trial                 1702   1203
2627                              trial                 1703   1203
2628                     f?ll?w   follow                1704   1204
2629                     write.   writ_.                1705   1205
2630                   Hearstep   H_ar                  1706   1206
2631                   Hearstep           ∅-2           1706   None
2632                   Hearstep   st_p                  1706   1207
2633                              st_p                  1707   1207
2634                   fund.B?y   Boy                   1708   1209
2635                   fund.B?y   fund.                 1708   1208
2636                     n?tice   notic_                1709   1210
2637                      ab?ve   abov_                 1710   1211
2638                      begin   b_gin                 1711   1212
2639                      begin           ∅-2           1711   None
2640                              b_gin                 1712   1212
2641                      fl??r   floor                 1713   1213
2642           public.C?mmunity   Community             1714   1215
2643           public.C?mmunity   public.               1714   1214
2644                        far   far                   1715   1216
2645                      green   gr__n                 1716   1217
2646                      green           ∅-2           1716   None
2647                              gr__n                 1717   1217
2648             necessaryhand.   hand.                 1718   1219
2649             necessaryhand.   n_c_ssary             1718   1218
2650             necessaryhand.           ∅-2           1718   None
2651                              hand.                 1719   1219
2652                  Directi?n   Dir_ction             1720   1220
2653          w?ndereye.Instead           ∅-2           1721   None
2654          w?ndereye.Instead   wond_r                1721   1221
2655                    federal           ∅-2           1722   None
2656                      gr?up           ∅-2           1723   None
2657                                      ∅-2           1724   None
2658                    student           ∅-2           1725   None
2659                     skill.           ∅-2           1726   None
2660                    Defense           ∅-2           1727   None
2661                       blue           ∅-2           1728   None
2662                         g?           ∅-2           1729   None
2663             cust?mertrade.           ∅-2           1730   None
2664                     Expert           ∅-2           1731   None
2665                     Expert   wond_r                1731   1221
2666                              _y_.Th_ms_lv_s        1732   1222
2667              y?urc?mputer.           ∅-2           1733   None
2668              y?urc?mputer.   _y_.Th_ms_lv_s        1733   1222
2669                                      ∅-2           1734   None
2670                Firmbecause           ∅-2           1735   None
2671                  religi?us           ∅-2           1736   None
2672                       half           ∅-2           1737   None
2673                                      ∅-2           1738   None
2674                       feel           ∅-2           1739   None
2675                  t?ugh?wn.           ∅-2           1740   None
2676                                      ∅-2           1741   None
2677                    Mrsm?ve           ∅-2           1742   None
2678                       read           ∅-2           1743   None
2679                                      ∅-2           1744   None
2680        artistherself.White           ∅-2           1745   None
2681                                      ∅-2           1746   None
2682                piecemeth?d           ∅-2           1747   None
2683                                      ∅-2           1748   None
2684              ?fdem?cratic.           ∅-2           1749   None
2685                                      ∅-2           1750   None
2686                   American           ∅-2           1751   None
2687                      still           ∅-2           1752   None
2688                       ?nt?           ∅-2           1753   None
2689                safec?ntain           ∅-2           1754   None
2690                                      ∅-2           1755   None
2691            languageartist.           ∅-2           1756   None
2692                                      ∅-2           1757   None
2693              Financialbill           ∅-2           1758   None
2694                                      ∅-2           1759   None
2695                    seri?us           ∅-2           1760   None
2696              empl?yeething           ∅-2           1761   None
2697                       arm.           ∅-2           1762   None
2698                   Painting           ∅-2           1763   None
2699                                      ∅-2           1764   None
2700                ?pp?rtunity           ∅-2           1765   None
2701          internati?nal?ver           ∅-2           1766   None
2702                                      ∅-2           1767   None
2703                    partshe           ∅-2           1768   None
2704                                      ∅-2           1769   None
2705         d?g.Themselvesmiss           ∅-2           1770   None
2706         d?g.Themselvesmiss   _y_.Th_ms_lv_s        1770   1222
2707         d?g.Themselvesmiss   miss                  1770   1223
2708                              miss                  1771   1223
2709                    acc?unt   account               1772   1224
2710                   ifsp?rt.   sport.                1773   1226
2711                   ifsp?rt.   if                    1773   1225
2712                       G?al   Goal                  1774   1227
2713                    himself           ∅-2           1775   None
2714                    himself   hims_lf               1775   1228
2715                              hims_lf               1776   1228
2716                     sister   sist_r                1777   1229
2717                     least.   l_ast.                1778   1230
2718                      Gr?up   Group                 1779   1231
2719                     d?ct?r   doctor                1780   1232
2720                chargew?uld           ∅-2           1781   None
2721                chargew?uld   charg_                1781   1233
2722                chargew?uld   would                 1781   1234
2723                              would                 1782   1234
2724                     bey?nd   b_yond                1783   1235
2725                enj?ycenter   c_nt_r                1784   1237
2726                enj?ycenter   _njoy                 1784   1236
2727                 while.Able   whil_.Abl_            1785   1238
2728                     threat   thr_at                1786   1239
2729                      teach   t_ach                 1787   1240
2730                       high   high                  1788   1241
2731                       high           ∅-2           1788   None
2732                              high                  1789   1241
2733                     church   church                1790   1242
2734                 callthing.   call                  1791   1243
2735                 callthing.   thing.                1791   1244
2736                    Present           ∅-2           1792   None
2737                    Present   Pr_s_nt               1792   1245
2738                              Pr_s_nt               1793   1245
2739                     career   car__r                1794   1246
2740                       yeah   y_ah                  1795   1247
2741                up?nagency.   upon                  1796   1248
2742                up?nagency.   ag_ncy.               1796   1249
2743                     Single   Singl_                1797   1250
2744                       t?wn   town                  1798   1251
2745                       t?wn           ∅-2           1798   None
2746                              town                  1799   1251
2747             certainlysh?rt   c_rtainly             1800   1252
2748             certainlysh?rt           ∅-2           1800   None
2749             certainlysh?rt   short                 1800   1253
2750                              short                 1801   1253
2751                 thank.Size   thank.                1802   1254
2752                 thank.Size   Siz_                  1802   1255
2753                              Siz_                  1803   1255
2754                        bad   bad                   1804   1256
2755               s?urcef?cus.           ∅-2           1805   None
2756               s?urcef?cus.   sourc_                1805   1257
2757               s?urcef?cus.   focus.                1805   1258
2758                              focus.                1806   1258
2759             C?ntinueaffect   Continu_              1807   1259
2760             C?ntinueaffect   aff_ct                1807   1260
2761                     arrive   arriv_                1808   1261
2762                   pressure   pr_ssur_              1809   1262
2763                   pressure           ∅-2           1809   None
2764                              pr_ssur_              1810   1262
2765              apply?fficial   official              1811   1264
2766              apply?fficial   apply                 1811   1263
2767            prepare.Pattern           ∅-2           1812   None
2768            prepare.Pattern   pr_par_.Discuss       1812   1265
2769                                      ∅-2           1813   None
2770                       idea           ∅-2           1814   None
2771                    ?utside           ∅-2           1815   None
2772               evening.Half           ∅-2           1816   None
2773                  scientist           ∅-2           1817   None
2774                      there           ∅-2           1818   None
2775                                      ∅-2           1819   None
2776                     appear           ∅-2           1820   None
2777                  artn?tice           ∅-2           1821   None
2778                                      ∅-2           1822   None
2779         service.P?pulars?n           ∅-2           1823   None
2780                                      ∅-2           1824   None
2781            dem?cratic.Team           ∅-2           1825   None
2782                                      ∅-2           1826   None
2783                     myself           ∅-2           1827   None
2784           service.Disc?ver           ∅-2           1828   None
2785                       part           ∅-2           1829   None
2786                                      ∅-2           1830   None
2787                  direct?r.           ∅-2           1831   None
2788                    F??tper           ∅-2           1832   None
2789                   f?reign.           ∅-2           1833   None
2790                       Late           ∅-2           1834   None
2791                                      ∅-2           1835   None
2792               hearmarriage           ∅-2           1836   None
2793                                      ∅-2           1837   None
2794                 understand           ∅-2           1838   None
2795            several.Discuss   pr_par_.Discuss       1839   1265
2796            several.Discuss           ∅-2           1839   None
2797                       plan   plan                  1840   1266
2798                       view   vi_w                  1841   1267
2799                       wish   wish                  1842   1268
2800                  plant.J?b   Job                   1843   1270
2801                  plant.J?b   plant.                1843   1269
2802                       c?st   cost                  1844   1271
2803                      fear.   f_ar.                 1845   1272
2804                      W?rry   Worry                 1846   1273
2805                      W?rry           ∅-2           1846   None
2806                              Worry                 1847   1273
2807                    suchMrs   Mrs                   1848   1275
2808                    suchMrs   such                  1848   1274
2809                    suchMrs           ∅-2           1848   None
2810                              Mrs                   1849   1275
2811                        t??   too                   1850   1276
2812                       kn?w   know                  1851   1277
2813          betweeneverything           ∅-2           1852   None
2814          betweeneverything   b_tw__n               1852   1278
2815          betweeneverything   _v_rything            1852   1279
2816                              _v_rything            1853   1279
2817              kn?w.Ats?cial           ∅-2           1854   None
2818              kn?w.Ats?cial   know.At               1854   1280
2819              kn?w.Ats?cial   social                1854   1281
2820                              social                1855   1281
2821              churchfather.           ∅-2           1856   None
2822              churchfather.   church                1856   1282
2823              churchfather.   fath_r.               1856   1283
2824                              fath_r.               1857   1283
2825                     Future   Futur_                1858   1284
2826                 understand   und_rstand            1859   1285
2827           abilitycertainly   c_rtainly             1860   1287
2828           abilitycertainly   ability               1860   1286
2829                        sit   sit                   1861   1288
2830                      speak           ∅-2           1862   None
2831                      speak   sp_ak                 1862   1289
2832                              sp_ak                 1863   1289
2833                    seas?n.   s_ason.               1864   1290
2834                    Subject   Subj_ct               1865   1291
2835                       pull   pull                  1866   1292
2836                    ?utside   outsid_               1867   1293
2837                realityrace   rac_                  1868   1295
2838                realityrace   r_ality               1868   1294
2839                      p?int   point                 1869   1296
2840                    suffer.   suff_r.               1870   1297
2841                    suffer.           ∅-2           1870   None
2842                              suff_r.               1871   1297
2843                      Three   Thr__                 1872   1298
2844                 verywind?w           ∅-2           1873   None
2845                 verywind?w   v_ry                  1873   1299
2846                 verywind?w   window                1873   1300
2847                              window                1874   1300
2848          remembereducati?n   _ducation             1875   1302
2849          remembereducati?n   r_m_mb_r              1875   1301
2850                       l?ng   long                  1876   1303
2851                     maybe.   mayb_.                1877   1304
[match] finished in 367 ms
1879
```
# Contribute

If there is something bad about it, contact me on the issue tracker or via mail

# License

This is licensed under the GPL v3 license, in favor of all these good code example we learn from.
