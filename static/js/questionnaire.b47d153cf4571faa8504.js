webpackJsonp([1],{"2wBO":function(t,e,n){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var o={};n.d(o,"setInfo",function(){return P}),n.d(o,"setNav",function(){return V}),n.d(o,"setLoginDialogStatus",function(){return z});var i={};n.d(i,"userInfo",function(){return j}),n.d(i,"loginDialogOpen",function(){return G});var r=n("IvJb"),a={render:function(){var t=this.$createElement,e=this._self._c||t;return e("div",{attrs:{id:"warp-box"}},[e("router-view")],1)},staticRenderFns:[]};var s=n("C7Lr")(null,a,!1,function(t){n("FOKY")},null,null).exports,l=(n("Ambv"),n("zO6J")),c={render:function(){var t=this.$createElement,e=this._self._c||t;return e("div",[e("router-view",{attrs:{name:"head"}}),this._v(" "),e("router-view",{attrs:{name:"content"}}),this._v(" "),e("router-view",{attrs:{name:"footer"}})],1)},staticRenderFns:[]};var u=n("C7Lr")({name:"app"},c,!1,function(t){n("n1lr")},"data-v-741ef5ce",null).exports,f=n("ZHh2"),d=n("4Xi4"),m=n.n(d),p=n("aozt"),h=n.n(p),g="https://www.zhiliangku.com",v={setCookie:function(t,e,n){var o=new Date;o.setTime(o.getTime()+n),o.setDate(o.getDate()+n),document.cookie=t+"="+escape(e)+(null==n?"":";expires="+o.toUTCString())},getCookie:function(t){var e,n=new RegExp("(^| )"+t+"=([^;]*)(;|$)");return(e=document.cookie.match(n))?unescape(e[2]):null},delCookie:function(t){var e=new Date;e.setTime(e.getTime()-1),null!=v.getCookie(t)&&(document.cookie=t+"=; expires=Thu, 01 Jan 1970 00:00:01 GMT;")}},_=v,b={name:"login",created:function(){},computed:{dialogFormVisible:function(){return this.$store.state.loginDialogOpen}},data:function(){return{loginDialogOpen:!1,number:0,count_down_time:0,disabled:!1,btnContent:"获取验证码",loginRules:{code:[{validator:function(t,e,n){""===e?n(new Error("请输入短信验证码")):n()},trigger:"blur"}],mobile:[{validator:function(t,e,n){if(!e)return n(new Error("手机号必填"));setTimeout(function(){m()(e)?/^[1][3,4,5,7,8,9][0-9]{9}$/.test(e)?n():n(new Error("请输入正确的手机号码")):n(new Error("请输入数字值"))},1e3)},trigger:"blur"}],user:[{validator:function(t,e,n){""===e?n(new Error("请输入用户名")):n()},trigger:"blur"}]},loginForm:{code:"",mobile:"",user:""}}},methods:{hidenLoginDialog:function(){this.$refs.loginForm.resetFields(),this.$store.dispatch("setLoginDialogStatus",!1)},sendCodeErrorNotify:function(){this.$notify({title:"错误",message:"验证码发送失败,请输入正确的手机号码"})},code_error:function(){this.$notify({title:"错误",message:"验证码输入错误"})},sendCodeSucNotify:function(){this.$notify({title:"成功",message:"验证码发送成功",type:"success"})},sendCode:function(){var t,e=this;(t={phone:e.loginForm.mobile},h.a.post(g+"/sms_code/",t)).then(function(t){switch(t.status){case 201:e.sendCodeSucNotify();break;case 400:e.sendCodeErrorNotify();break;default:e.sendCodeErrorNotify()}})},countDown:function(){this.count_down_time>0?(this.count_down_time--,this.btnContent="重新获取("+this.count_down_time+"s)",setTimeout(this.countDown,1e3)):(this.count_down_time=60,this.btnContent="获取验证码",this.disabled=!1)},checkMobile:function(){this.loginForm.mobile&&/^[1][3,4,5,7,8,9][0-9]{9}$/.test(this.loginForm.mobile)?(this.count_down_time=60,this.disabled=!0,this.countDown(),this.sendCode()):this.sendCodeErrorNotify()},loginSucNotify:function(){this.$notify({title:"成功",message:"登录成功,可以开始答题了.",type:"success"})},login:function(){var t=this,e=this;e.$refs.loginForm.validate(function(n){var o;n&&(o={mobile:t.loginForm.mobile,code:t.loginForm.code,name:t.loginForm.user},h.a.post(g+"/quick_login/",o)).then(function(n){_.setCookie("name",n.data.name,1),_.setCookie("token",n.data.token,1),e.$store.dispatch("setInfo"),t.hidenLoginDialog()}).catch(function(t){e.code_error()})})}}},y={render:function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("el-dialog",{attrs:{title:"登录",visible:t.dialogFormVisible,center:"","before-close":t.hidenLoginDialog},on:{"update:visible":function(e){t.dialogFormVisible=e}}},[n("el-form",{ref:"loginForm",staticClass:"demo-ruleForm",attrs:{model:t.loginForm,"status-icon":"",rules:t.loginRules,"label-width":"100px"}},[n("el-form-item",{attrs:{label:"手机号",prop:"mobile"}},[n("el-input",{attrs:{type:"tel",disabled:t.disabled},model:{value:t.loginForm.mobile,callback:function(e){t.$set(t.loginForm,"mobile",t._n(e))},expression:"loginForm.mobile"}})],1),t._v(" "),n("el-form-item",{attrs:{label:"姓名",prop:"user"}},[n("el-input",{attrs:{type:"text"},model:{value:t.loginForm.user,callback:function(e){t.$set(t.loginForm,"user",e)},expression:"loginForm.user"}})],1),t._v(" "),n("el-form-item",{attrs:{label:"验证码",prop:"code"}},[n("el-input",{attrs:{type:"text"},model:{value:t.loginForm.code,callback:function(e){t.$set(t.loginForm,"code",e)},expression:"loginForm.code"}}),t._v(" "),n("el-button",{attrs:{type:"primary",disabled:t.disabled},on:{click:t.checkMobile}},[t._v("\n        "+t._s(t.btnContent)+"\n      ")])],1)],1),t._v(" "),n("div",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[n("el-button",{on:{click:t.hidenLoginDialog}},[t._v("取消")]),t._v(" "),n("el-button",{attrs:{type:"primary"},on:{click:t.login}},[t._v("登录")])],1)],1)},staticRenderFns:[]};var k=n("C7Lr")(b,y,!1,function(t){n("Fq35")},"data-v-726ccaa0",null).exports,w={name:"loginHead",components:{login:k},computed:{username:function(){var t=this.$store.state.userInfo.name;return t?t.replace(/^(\d{3})\d{4}(\d{4})$/,"$1****$2"):""}},created:function(){},data:function(){return{}},methods:{showLoginDialog:function(){this.$store.dispatch("setLoginDialogStatus",!0)},loginOut:function(){_.delCookie("token"),_.delCookie("name"),this.$store.dispatch("setInfo")}}},q={render:function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",[t.username?t._e():n("el-button",{attrs:{type:"text"},on:{click:t.showLoginDialog}},[n("span",[t._v("登录")])]),t._v(" "),t.username?n("div",[n("span",{staticClass:"username"},[t._v("欢迎您 , "+t._s(t.username)+"  ")]),t._v(" "),n("el-button",{staticClass:"username",attrs:{type:"text"},on:{click:t.loginOut}},[t._v("退出")]),t._v(" "),n("hr")],1):t._e(),t._v(" "),n("login")],1)},staticRenderFns:[]};var C=n("C7Lr")(w,q,!1,function(t){n("zjvt")},"data-v-112b028a",null).exports,F=n("3cXf"),$=n.n(F),L={arrMap:function(t,e,n){if(t)return t.map(function(t,o){var i=t.slice(4,6);if(i>e&&i<n)return t})},arrMap2:function(t){if(t)return t.map(function(t,e){if(t)return t.slice(2,6)+":"+t.slice(0,2)})},arrsLice:function(t){for(var e=[],n=0;n<t.length;n++)void 0!==t[n]&&e.push(t[n]);return e}},D={name:"questionnaire",components:{login:k},data:function(){return{submitType:"",src:"",formLabelWidth:"120px",teacherDialog:!1,activeName:"second",eq_results:[],iq_results:[],eq_radio:[],iq_radio:[],answer:"",eqFraction:"",iqLogic:"",phone:"",teachers:[],teacher_form:{users:""}}},methods:{showlLoginDialog:function(){this.$store.getters.userInfo.token||this.$store.dispatch("setLoginDialogStatus",!0)},notAnswerNotify:function(){this.$notify.error({title:"请注意",message:"请先做题."})},warningNotify:function(){this.$notify({title:"警告",message:"请稍后再试",type:"warning"})},AnswerOkNotify:function(){this.$notify({title:"成功",message:"恭喜,答题成功,稍后通知答题结果",type:"success"})},notSelectTeacherNotify:function(){this.$notify.error({title:"失败",message:"请选择咨询老师."})},getConsultant:function(){var t=this;h.a.get(g+"/consultant/").then(function(e){switch(e.status){case 200:t.teachers=e.data.results;break;case 400:t.sendCodeErrorNotify();break;default:t.sendCodeErrorNotify()}})},handOver:function(t){this.submitType=t,this.$store.getters.userInfo.token?"eq"==t&&!this.eqFraction||"iq"==t&&!this.iqLogic?this.notAnswerNotify():(this.teacherDialog=!0,this.getConsultant()):this.$store.dispatch("setLoginDialogStatus",!0)},submitTestPaper:function(){"eq"==this.submitType?this.submitEq():"iq"==this.submitType&&this.submitIq()},submitEq:function(){if(this.eqFraction)var t=this.eqFraction.map(function(t){return+t});if(t)var e=t.reduce(function(t,e,n){return t+e});var n,o=this;o.teacher_form.users?(n={category:"eq",value:e,consultant_email:o.teacher_form.users},h.a.post(g+"/eq/",n)).then(function(t){switch(t.status){case 201:o.AnswerOkNotify(),o.teacherDialog=!1;break;default:o.warningNotify()}}):o.notSelectTeacherNotify()},submitIq:function(){for(var t=this,e=t.iqLogic,n=L.arrMap(e,0,11),o=L.arrMap(e,10,21),i=L.arrMap(e,20,31),r=L.arrMap(e,30,41),a=L.arrMap(e,40,51),s=L.arrMap(e,50,61),l=L.arrMap2(n),c=L.arrMap2(o),u=L.arrMap2(i),f=L.arrMap2(r),d=L.arrMap2(a),m=L.arrMap2(s),p=L.arrsLice(l),v=L.arrsLice(c),_=L.arrsLice(u),b=L.arrsLice(f),y=L.arrsLice(d),k=L.arrsLice(m),w={},q=0;q<p.length;q++){var C=p[q].split(":");w[C[0]]=C[1]}var F=$()(w),D={};for(q=0;q<v.length;q++){var N=v[q].split(":");D[N[0]]=N[1]}var x=$()(D),O={};for(q=0;q<_.length;q++){var T=_[q].split(":");O[T[0]]=T[1]}var E=$()(O),I={};for(q=0;q<b.length;q++){var M=b[q].split(":");I[M[0]]=M[1]}I.TI38=this.answer;var S=$()(I),A={};for(q=0;q<y.length;q++){var R=y[q].split(":");A[R[0]]=R[1]}var P=$()(A),V={};for(q=0;q<k.length;q++){var z=k[q].split(":");V[z[0]]=z[1]}var j,G=$()(V);localStorage.getItem("token");t.teacher_form.users?(j={category:"iq",option_1:F,option_2:x,option_3:E,option_4:S,option_5:P,option_6:G,consultant_email:t.teacher_form.users},h.a.post(g+"/iq/",j)).then(function(e){switch(e.status){case 201:t.AnswerOkNotify(),t.teacherDialog=!1;break;default:t.warningNotify()}}):t.notSelectTeacherNotify()}},watch:{eq_radio:function(t){this.eqFraction=t},iq_radio:function(t){this.iqLogic=t}},created:function(){var t=this;h.a.get(g+"/eq/").then(function(e){t.eq_results=e.data.results}),h.a.get(g+"/iq/").then(function(e){t.iq_results=e.data.results})}},N={render:function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",[n("el-tabs",{model:{value:t.activeName,callback:function(e){t.activeName=e},expression:"activeName"}},[n("el-tab-pane",{attrs:{label:"职场素质",name:"second"}},[t._l(t.eq_results,function(e,o){return n("div",{key:o,on:{click:t.showlLoginDialog}},[n("el-col",{staticClass:"card",attrs:{span:24}},[n("el-card",{attrs:{shadow:"hover"}},[n("p",[t._v(t._s(e.title))]),t._v(" "),n("el-radio-group",{model:{value:t.eq_radio[o],callback:function(e){t.$set(t.eq_radio,o,e)},expression:"eq_radio[index]"}},t._l(e.option,function(e,o){return n("el-radio",{key:o,attrs:{label:e.value}},[t._v(t._s(e.option))])}))],1)],1)],1)}),t._v(" "),n("el-button",{attrs:{type:"primary"},on:{click:function(e){t.handOver("eq")}}},[t._v("交卷")])],2),t._v(" "),n("el-tab-pane",{attrs:{label:"逻辑能力"}},[t._l(t.iq_results,function(e,o){return n("div",{key:o,staticClass:"cards",on:{click:t.showlLoginDialog}},[n("el-col",{attrs:{span:24}},[n("el-card",{staticClass:"el",attrs:{shadow:"hover"}},[n("p",[t._v(t._s(e.title))]),t._v(" "),-1!=e.title.indexOf("38")?n("input",{directives:[{name:"model",rawName:"v-model",value:t.answer,expression:"answer"}],attrs:{type:"text",name:"",placeholder:"请输入你的答案"},domProps:{value:t.answer},on:{input:function(e){e.target.composing||(t.answer=e.target.value)}}}):t._e(),t._v(" "),n("p",[n("img",{attrs:{src:e.image}})]),t._v(" "),n("el-radio-group",{model:{value:t.iq_radio[o],callback:function(e){t.$set(t.iq_radio,o,e)},expression:"iq_radio[index]"}},t._l(e.option,function(e,o){return n("el-radio",{key:o,attrs:{label:e.value+e.titleno}},[n("p",[t._v(t._s(e.option))])])}))],1)],1)],1)}),t._v(" "),n("el-button",{attrs:{type:"primary"},on:{click:function(e){t.handOver("iq")}}},[t._v("交卷")])],2)],1),t._v(" "),n("el-dialog",{attrs:{title:"选择老师帮你解析答案",visible:t.teacherDialog},on:{"update:visible":function(e){t.teacherDialog=e}}},[n("el-form",{attrs:{model:t.teacher_form}},[n("el-form-item",{attrs:{label:"老师","label-width":t.formLabelWidth}},[n("el-select",{attrs:{placeholder:"请选择老师",value:""},model:{value:t.teacher_form.users,callback:function(e){t.$set(t.teacher_form,"users",e)},expression:"teacher_form.users"}},t._l(t.teachers,function(e,o){return n("el-option",{key:o,attrs:{value:e.email}},[t._v("\n            "+t._s(e.name)+"\n          ")])}))],1)],1),t._v(" "),n("div",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[n("el-button",{on:{click:function(e){t.teacherDialog=!1}}},[t._v("取消")]),t._v(" "),n("el-button",{attrs:{type:"primary"},on:{click:t.submitTestPaper}},[t._v("确定")])],1)],1),t._v(" "),n("login")],1)},staticRenderFns:[]};var x=n("C7Lr")(D,N,!1,function(t){n("pi7V")},null,null).exports;r.default.use(l.a);var O,T=new l.a({routes:[{path:"/app",component:u,children:[{path:"questionnaire",name:"questionnaire",components:{head:C,content:x,footers:f.default},meta:{title:"登录",need_log:!1}}]},{path:"/",redirect:"/app/questionnaire"}]}),E=n("9rMa"),I=n("a3Yh"),M=n.n(I);r.default.prototype.$http=h.a;var S=(O={},M()(O,"SET_INFO",function(t){t.userInfo={name:_.getCookie("name"),token:_.getCookie("token")}}),M()(O,"SET_LOGINDIALOGOPEN",function(t,e){t.loginDialogOpen=e}),O),A={userInfo:{name:_.getCookie("name")||"",token:_.getCookie("token")||""},loginDialogOpen:!1};function R(t){return function(e){for(var n=arguments.length,o=Array(n>1?n-1:0),i=1;i<n;i++)o[i-1]=arguments[i];return e.commit.apply(void 0,[t].concat(o))}}var P=R("SET_INFO"),V=R("SET_NAV"),z=R("SET_LOGINDIALOGOPEN"),j=function(t){return t.userInfo},G=function(t){return t.loginDialogOpen};r.default.use(E.a);var Y=new E.a.Store({state:A,mutations:S,actions:o,getters:i}),H=n("rVsN"),J=n.n(H);h.a.interceptors.request.use(function(t){return Y.state.userInfo.token&&(t.headers.Authorization="Bearer "+Y.state.userInfo.token),t},function(t){return J.a.reject(t)}),h.a.defaults.headers.post["Content-Type"]="application/x-www-form-urlencoded; charset=UTF-8",h.a.interceptors.response.use(void 0,function(t){return t.response.status,J.a.reject(t.response.data)});var W=n("H93t"),B=n.n(W);n("TsY+");r.default.prototype.$http=h.a,r.default.use(B.a),r.default.config.productionTip=!1,new r.default({el:"#app",router:T,store:Y,components:{App:s},template:"<App/>"})},Ambv:function(t,e){},Cq93:function(t,e,n){"use strict";var o={render:function(){var t=this.$createElement;return(this._self._c||t)("div")},staticRenderFns:[]};e.a=o},FOKY:function(t,e){},Fq35:function(t,e){},IPWu:function(t,e){},"TsY+":function(t,e){},ZHh2:function(t,e,n){"use strict";var o=n("mi86"),i=n.n(o),r=n("Cq93");var a=function(t){n("IPWu")},s=n("C7Lr")(i.a,r.a,!1,a,"data-v-fa2dcbb0",null);e.default=s.exports},mi86:function(t,e){},n1lr:function(t,e){},pi7V:function(t,e){},zjvt:function(t,e){}},["2wBO"]);
//# sourceMappingURL=questionnaire.b47d153cf4571faa8504.js.map