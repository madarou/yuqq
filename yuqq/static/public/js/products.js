var Products = (function(products) {
	var prod = function(products){
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
	prod.prototype={
			init:function(){
				_initData(this,products);
			},
			showItems:function(target){
				var list = this.get('productList');
				var content = '<span_3>';
				for(var i=0;i<list.length;i++){
					content += _setItem(list[i]);
					if(i%3==2){
						content += '<div class="clearfix"></div></span_3><span_3>'
					}
				}
				target.html(content+'<div class="clearfix"></div></span_3>');
			}
	}
	//本应从服务器读取的，但django在页面加载时已经返回了数据，不用再单独请求，
	//所以将已经随页面加载时返回的数据serverdata直接传进来
	var _initData = function(that,products){
		that.set('productList',products);
	}
	
	var _setItem = function(obj){
		var item = '<div class="col_1_of_single1 span_1_of_single1">';
		var img = '<a href="/detail/'+obj['fields']['name']+'"> <img src="/static/'+obj['fields']['pic5']+'" class="img-responsive"/></a>';
		var name = '<h3>'+obj['fields']['name']+'</h3>';
		var slogan = '<p>'+obj['fields']['slogan']+'</p>';
		var price = '<a class="btn1 btn6 btn-1 btn1-1b buy" style="margin-top:0px;padding: 3px 20px">'+obj['fields']['price_low']+'</a>';
		var view_detail = '<a href="/detail/'+obj['fields']['name']+'" style="font-size:50%;margin-left: 1em;">详情</a>';
		return item+img+name+slogan+price+view_detail+'</div>';
	}
	return prod;
})(products_server);