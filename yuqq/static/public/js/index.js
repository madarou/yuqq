var Index = (function(products) {
	var index = function(products){
		this.config={
			productList:''
		}
		this.set=function(key,value){
			this.config[key]=value;
		}
		this.get=function(key){
			return this.config[key];
		}
		this.init();
	}
	index.prototype={
			init:function(){
				_initData(this,products);
			},
			showPro1:function(target){
				var pro1 = this.get('productList')[0]['fields'];
				var img = '<img src="/static/'+pro1['pic']+'" class="img-responsive"/>';
				var div1 = '<div class="banner_desc">';
				var name = '<h1><a href="/detail/'+pro1['name']+'" style="color:#e05b5b">'+pro1['name']+'</a></h1>';
				var slogan = '<h2>'+pro1['slogan']+'</h2>';
				var price = '<h5>￥'+pro1['price']+'起 <small>Only</small></h5>';
				var div2 = '<a class="btn1 btn4 btn-1 btn1-1b buy">求包养</a></div>';
				target.html(img+div1+name+slogan+price+div2);
			},
			showPro23:function(target){
				var pro2 = this.get('productList')[1]['fields'];
				var pro3 = this.get('productList')[2]['fields'];
				var li2 = '<li><a href="/detail/'+pro2['name']+'"><img src="/static/'+pro2['pic']+'"/></a></li>';
				var li3 = '<li><a href="/detail/'+pro3['name']+'"><img src="/static/'+pro3['pic']+'"/></a></li>';
				target.html(li2+li3);
			},
			showPro48:function(target){
				var pro4 = this.get('productList')[3]['fields'];
				var pro5 = this.get('productList')[4]['fields'];
				var pro6 = this.get('productList')[5]['fields'];
				var pro7 = this.get('productList')[6]['fields'];
				var pro8 = this.get('productList')[7]['fields'];
				var li4 = '<a href="/detail/'+pro4['name']+'"><li><img src="/static/'+pro4['pic']+'" class="img-responsive"/> <span class="btn5">'+pro4['price']+'</span><p>'+pro4['name']+'</p></li></a>';
				var li5 = '<a href="/detail/'+pro5['name']+'"><li><img src="/static/'+pro5['pic']+'" class="img-responsive"/> <span class="btn5">'+pro5['price']+'</span><p>'+pro5['name']+'</p></li></a>';
				var li6 = '<a href="/detail/'+pro6['name']+'"><li><img src="/static/'+pro6['pic']+'" class="img-responsive"/> <span class="btn5">'+pro6['price']+'</span><p>'+pro6['name']+'</p></li></a>';
				var li7 = '<a href="/detail/'+pro7['name']+'"><li><img src="/static/'+pro7['pic']+'" class="img-responsive"/> <span class="btn5">'+pro7['price']+'</span><p>'+pro7['name']+'</p></li></a>';
				var li8 = '<a href="/detail/'+pro8['name']+'"><li><img src="/static/'+pro8['pic']+'" class="img-responsive"/> <span class="btn5">'+pro8['price']+'</span><p>'+pro8['name']+'</p></li></a>';
				target.html(li4+li5+li6+li7+li8+'<div class="clearfix"></div>');
			},
			showPro910:function(target){
				var pro9 = this.get('productList')[8]['fields'];
				var pro10 = this.get('productList')[9]['fields'];
				var div1 = '<div class="col_1_of_2 span_1_of_2"><a href="/detail/'+pro9['name']+'"><img src="/static/'+pro9['pic']+'" class="img-responsive"/></a></div>';
				var div2 = '<div class="col_1_of_2 span_1_of_2"><a href="/detail/'+pro10['name']+'"><img src="/static/'+pro10['pic']+'" class="img-responsive"/></a></div>';
				target.html(div1+div2+'<div class="clearfix"></div>');
			},
			showPro11:function(target){
				var pro11 = this.get('productList')[10]['fields'];
				var div1 = '<div class="col_1_of_2 span_1_of_2 span_3"><h3><a href="/products/none/yugang/" style="color:#e05b5b">'+pro11['name']+'</a></h3><h4>￥'+pro11['price']+'</h4><h5 style="font-size:18px">'+pro11['slogan']+'</h5><a class="btn1 btn6 btn-1 btn1-1b buy" style="margin-top:1em">带走</a></div>';
				var div2 = '<div class="col_1_of_2 span_1_of_2 span_4"><div class="span_5"><img src="/static/'+pro11['pic']+'" class="img-responsive"/></div></div>';
				target.html(div1+div2+'<div class="clearfix"></div>');
			}
	}
	//本应从服务器读取的，但django在页面加载时已经返回了数据，不用再单独请求，
	//所以将已经随页面加载时返回的数据serverdata直接传进来
	var _initData = function(that,products){
		that.set('productList',products);
	}

	return index;
})(index_server);