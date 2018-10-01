<template>
	<div class="contenter">
		<!-- 是否退出 -->
		<div class="Logbtn">
			<el-button @click="dialogFormVisible = true" class="Logbtns">登录</el-button>
			<span @click="phones">{{phone}}
			</span>
			<div class="out" v-show="dele">
				<span @click="Sign">退出</span>
				<span @click="cancel">取消</span>
			</div>
		</div>
		<el-dialog title="登录" :visible.sync="dialogFormVisible" center>
			<!-- 插入测试 -->
			<el-form :model="ruleForm2" status-icon :rules="rules2" ref="ruleForm2" label-width="100px" class="demo-ruleForm">
				<el-form-item label="手机号" prop="num">
					<el-input v-model.number="ruleForm2.num"></el-input>
				</el-form-item>
				<el-form-item label="验证码" prop="code">
					<el-input type="tel" v-model="ruleForm2.code" auto-complete="off"></el-input>
					<el-button type="primary" @click="second">发送验证码</el-button>
				</el-form-item>
			</el-form>
			<!-- 插入测试 -->
			<div slot="footer" class="dialog-footer">
				<el-button @click="dialogFormVisible = false; resetForm('ruleForm2')">取 消</el-button>
				<el-button type="primary" @click="submitForm('ruleForm2')">登 录</el-button>
			</div>
		</el-dialog>
		<div>
			<el-tabs v-model="activeName">
				<el-tab-pane label="职场素质" name="second">
					<div v-for="(item,index) in results" :key="index" @click="btn">
						<el-col :span="24">
							<el-card shadow="hover">
								<p>{{item.title}}</p>
								<el-radio-group v-model="radio1[index]">
									<el-radio :label="key.value" v-for="(key,index) in item.option" :key="index">{{key.option}}</el-radio>
								</el-radio-group>
							</el-card>
						</el-col>
					</div>
					<button @click="test" class="entry">提交
					</button>
					<!-- 成功提示 -->
					<el-button :plain="true"></el-button>
					<el-button :plain="true"></el-button>
				</el-tab-pane>
				<el-tab-pane label="逻辑能力">
					<div v-for="(item,index) in results_iq" :key="index" @click="btn">
						<el-col :span="24">
							<el-card shadow="hover">
								<p>{{item.title}}</p>
								<p><img :src="item.image"></p>
								<el-radio-group v-model="radio2[index]">
									<el-radio :label="key.value + key.titleno" v-for="(key, index) in item.option" :key="index">
										<p>{{key.option}}</p>
									</el-radio>
								</el-radio-group>
							</el-card>
						</el-col>
					</div>
					<button @click="test_iq" class="entrys">提交</button>
				</el-tab-pane>
			</el-tabs>
		</div>
	</div>
</template>
<style type="text/css" lang="less" scoped>
* {
	padding: 0;
	margin: 0;
}

.contenter {
	width: 800px;
	margin: 0 auto;
	position: relative;
}

.contenter .Logbtn {
	width: 70px;
	height: 30px;
	font-size: 14px;
	position: relative;
	left: 810px;
	top: 35px;
}

.contenter .Logbtn .out {
	width: 40px;
	height: 40px;
	line-height: 40px;
	font-size: 15px;
}

.contenter .Logbtn .out span {
	width: 40px;
	height: 40px;
	text-align: center;
	border: 1px solid blue;
}

.contenter .Logbtn .out span:hover {
	background: #164C83;
	color: #ffffff;
}

.contenter .Logbtn .Logbtns {
	width: 70px;
	height: 30px;
	font-size: 14px;
}


.el-tabs {
	width: 800px;
	height: 20px;
}

.contenter .Logbtn span {
	display: block;
	width: 100px;
	height: 30px;
}

.entry,
.entrys {
	display: block;
	width: 100px;
	height: 40px;
	margin: 0;
	padding: 0;
	border: 1px solid transparent;
	outline: none;
	background: #0461C0;
	color: #FFF;
	position: relative;
	left: 300px;
}

.el-button.is-round {
	position: relative;
	left: 860px;
	top: 35px;
	width: 100px;
	height: 60px;
}

.el-button.is-round span {
	display: block;
	width: 100px;
	height: 60px;
	text-align: center;
}

.el-tabs__item {
	height: 50px;
}

</style>
<script type="text/javascript">
export default {
	data() {
		var checkNum = (rule, value, callback) => {
			if (!value) {
				return callback(new Error('账号不能为空'));
			}
			setTimeout(() => {
				if (!Number.isInteger(value)) {
					callback(new Error('请输入数字值'));
				} else {
					var myreg = /^[1][3,4,5,7,8][0-9]{9}$/;
					if (!myreg.test(value)) {
						callback(new Error('请输入正确的手机号码'));
					} else {
						callback();
					}

				}
			}, 1000);
		};
		var validatePass = (rule, value, callback) => {
			if (value === '') {
				callback(new Error('请输入短信验证码'));
			} else {

				callback();
			}
		};
		return {
			// 存储用户的职场素质分数
			Fraction: '',
			// 存储用户的逻辑能力的状态
			logic: '',
			// 退出显示
			dele: false,
			// 图片
			src: '',
			number: 0,
			// 显示用户手机号
			phone: '',
			activeName: 'second',
			// 职场素质的v-model
			radio1: [],
			// 逻辑能力的v-model
			radio2: [],
			// 记录职场素质的累计分手
			sum: 0,
			isActives: '0',
			// 循环的职场素质的数据
			results: [],
			// 循环的是逻辑能力的数据
			results_iq: [],
			// 存储用户手机号
			name: '',
			// 存储token值
			token: '',
			// loginPower: false,
			/*设定规则指向*/
			ruleForm2: {
				// 短信验证码
				code: '',
				// 手机验证码
				num: '',
				delivery: false,
			},
			rules2: {
				code: [
					{ validator: validatePass, trigger: 'blur' }
				],

				num: [
					{ validator: checkNum, trigger: 'blur' }
				]
			},
			/*插入form方法*/
			// dialogTableVisible: false,
			dialogFormVisible: false,
			form: {
				name: '',
				type: [],
				resource: '',
				desc: ''
			},
			formLabelWidth: '120px'
		};
	},
	// 监听数据变化
	watch: {
		// 监听的是职场素质的数据
		'radio1': function(val) {
			this.Fraction = val;
		},
		// 监听逻辑能力的数据
		'radio2': function(val) {
			this.logic = val;


		}

	},
	methods: {
		// 点击是否退出
		Sign() {
			localStorage.clear();
			this.phone = '';
			this.dele = false;
		},
		// 点击是否取消
		cancel() {
			this.dele = false;
		},
		// 退出
		phones() {
			this.dele = true;
		},
		// 提示成功消息
		open6() {
			this.$message({
				showClose: false,
				message: '恭喜你提交成功,请稍后再试',
				type: 'success'
			});

		},
		// 错误提示
		open8() {
			this.$message({
				showClose: true,
				message: '错了哦，答题失败,请稍后',
				type: 'error'
			});
		},
		// 检测用户是否登录过
		btn() {
			this.dialogFormVisible = true;
			if (this.phone) {
				this.dialogFormVisible = false;
			}

		},
		// 提交职场素质数据
		test() {
			if (this.Fraction) {
				var arr = this.Fraction.map(function(item) {
					return +item;
				})
			}
			if (arr) {
				var result = arr.reduce(function(result, value, index) {
					return result + value;
				});
			}

			// 获取token
			var str = localStorage.getItem('token');
			// token拼接
			var token = 'Bearer ' + str;
			// 备份this
			var self = this;
			$.ajax({
				type: "post",
				url: "http://www.zhiliangku.com/eq/",
				async: false,
				data: {
					category: 'eq',
					value: result
				},
				beforeSend: function(xhr) {
					xhr.setRequestHeader("Authorization", token)
				},
				dataType: 'json',
				success: function(data) {
					if (data.value !== '' && data.Status !== 201) {
						self.open6();
					} else {
						self.open8();
					}
				},
				error: function(data) {}
			});


		},
		// 提交逻辑能力数据
		test_iq() {
			// 获取的数据
			var arr = this.logic;

			var arr1 = this.arrmap(arr, 0, 11);
			var arr2 = this.arrmap(arr, 10, 21);
			var arr3 = this.arrmap(arr, 20, 31);
			var arr4 = this.arrmap(arr, 30, 41);
			var arr5 = this.arrmap(arr, 40, 51);
			var arr6 = this.arrmap(arr, 50, 61);

			var arry1 = this.arrmap2(arr1)
			var arry2 = this.arrmap2(arr2)
			var arry3 = this.arrmap2(arr3)
			var arry4 = this.arrmap2(arr4)
			var arry5 = this.arrmap2(arr5)
			var arry6 = this.arrmap2(arr6)

			var arrys1 = this.arrslice(arry1);
			var arrys2 = this.arrslice(arry2);
			var arrys3 = this.arrslice(arry3);
			var arrys4 = this.arrslice(arry4);
			var arrys5 = this.arrslice(arry5);
			var arrys6 = this.arrslice(arry6);
			// 第一条数据
			var a1 = {}
			for (var i = 0; i < arrys1.length; i++) {
				var str1 = arrys1[i].split(':');
				a1[str1[0]] = str1[1]
			}
			var b1 = JSON.stringify(a1)
			console.log(b1);
			// 第二条数据
			var a2 = {}
			for (var i = 0; i < arrys2.length; i++) {
				var str2 = arrys2[i].split(':');
				a2[str2[0]] = str2[1]
			}
			var b2 = JSON.stringify(a2)
			console.log(b2);
			// 第三条数据
			var a3 = {}
			for (var i = 0; i < arrys3.length; i++) {
				var str3 = arrys3[i].split(':');
				a3[str3[0]] = str3[1]
			}
			var b3 = JSON.stringify(a3)
			console.log(b3);
			// 第四条
			var a4 = {}
			for (var i = 0; i < arrys4.length; i++) {
				var str4 = arrys4[i].split(':');
				a4[str4[0]] = str4[1]
			}
			var b4 = JSON.stringify(a4)
			console.log(b4);
			// 第五条
			var a5 = {}
			for (var i = 0; i < arrys5.length; i++) {
				var str5 = arrys5[i].split(':');
				a5[str5[0]] = str5[1]
			}
			var b5 = JSON.stringify(a5)
			console.log(b5);
			var a6 = {}
			for (var i = 0; i < arrys6.length; i++) {
				var str6 = arrys6[i].split(':');
				a6[str6[0]] = str6[1]
			}
			var b6 = JSON.stringify(a6)
			console.log(b6);

			var str = localStorage.getItem('token');
			var token = 'Bearer ' + str;
			console.log(token);
			var self = this;
			$.ajax({
				type: "post",
				url: "http://www.zhiliangku.com/iq/",
				async: false,
				data: {
					category: 'iq',
					option_1: b1,
					option_2: b2,
					option_3: b3,
					option_4: b4,
					option_5: b5,
					option_6: b6
				},
				beforeSend: function(xhr) {
					xhr.setRequestHeader("Authorization", token)
				},
				dataType: 'json',
				success: function(data) {
				  if(data.value !== '' && data.Status !== 201) {
				  	self.open6();
				  } else{
				  	self.open8();
				  }
					console.log(data);
				},
				error: function(data) {
					console.log(data);
				}
			});

		},
		// 发送短信验证码接口
		second() {
			var self = this;
			self.ajaxSubmit.ajax({
				url: self.commmonWebConfig.zhiliangkuapi + self.ajaxSubmit.allUrl.message,
				type: "post",
				data: {
					phone: self.ruleForm2.num
				},
				async: false,
				dataType: 'json',
				success: function(data) {
					self.results = data.results;
				},
				error: function(data) {}

			})
		},
		// 提示用户登录信息
		submitForm(formName) {
			this.$refs[formName].validate((valid) => {
				if (valid) {
					this.$message({
						type: 'success',
						message: '登录成功'
					});
					this.dialogFormVisible = false;
				} else {
					this.$message({
						type: 'error',
						message: '登录失败,请重新输入'
					});
					return false;
				}

			});
			// 正则保护手机
			var reg = /^(\d{3})\d{4}(\d{4})$/;
			// 发送登录接口数据
			var self = this;
			self.ajaxSubmit.ajax({
				url: self.commmonWebConfig.zhiliangkuapi + self.ajaxSubmit.allUrl.login,
				type: "post",
				data: {
					// 携带的手机号码与短信验证码
					mobile: self.ruleForm2.num,
					code: self.ruleForm2.code,
				},
				async: false,
				dataType: 'json',
				success: function(data) {
					if (data.Status !== 201) {
						// 赋值token与手机号码
						self.token = data.token;
						self.name = data.name;

						// 在本地存储token与手机号码
						localStorage.setItem('token', self.token);
						localStorage.setItem('usernem', self.name);
						/*18146560703   5259*/
						// 取出并显示用户
						self.phone = localStorage.getItem('usernem');
						self.phone = self.phone.replace(reg, "$1****$2");
					}

				},
				// 失败之后执行的回调函数
				error: function(data) {

				}

			})

		},
		resetForm(formName) {
			this.$refs[formName].resetFields();
		}
	},
	created() {
		// 这里是eq向后台请求的数据
		var self = this;
		self.ajaxSubmit.ajax({
			url: self.commmonWebConfig.zhiliangkuapi + self.ajaxSubmit.allUrl.login_eq,
			type: "get",
			data: {

			},
			async: false,
			dataType: 'json',
			success: function(data) {
				self.results = data.results;
			},
			error: function(data) {}

		})
		// 这里是iq向后台请求的数据
		self.ajaxSubmit.ajax({
			url: self.commmonWebConfig.zhiliangkuapi + self.ajaxSubmit.allUrl.login_iq,
			type: "get",
			data: {

			},
			async: false,
			dataType: 'json',
			success: function(data) {
				self.results_iq = data.results;
			},
			error: function(data) {}

		})
	}
}

</script>
