//$.fn.extend({
//	showProductImgs:function(){
//		var list = {{ List|safe }};//放到extend里后{{}}会报错
//		this.html(list);
//	}
//})

var Detail = (function(product,intro) {
	var detail = function(product,intro){
		this.config={
			productObj:'',
			name:'',
			price_low:'',
			price_high:'',
			slogan:'',
			introduction:'',
			catalogue:'',
			inventory:'',
			time_to_market:'',
			pic1:'',
			pic2:'',
			pic3:'',
			pic4:'',
			pic5:'',
			related1:'',
			related2:'',
			related3:'',
			related4:'',
			popularity:'',
			remarks:'',
			//introduction fields
			brief_intro:'',
			raise_method:'',
			use_method:''
		}
		this.set=function(key,value){
			this.config[key]=value;
		}
		this.get=function(key){
			return this.config[key];
		}
		this.init();
	}
	detail.prototype={
			init:function(){
				_initData(this,product,intro);
			},
			setProductImgs:function(target){
				var img1_1 = '<img class="etalage_thumb_image img-responsive" src="/static/'+this.get('pic1')+'" />';
				var img1_2 = '<img class="etalage_source_image img-responsive" src="/static/'+this.get('pic1')+'" />';
				var img2_1 = '<img class="etalage_thumb_image img-responsive" src="/static/'+this.get('pic2')+'" />';
				var img2_2 = '<img class="etalage_source_image img-responsive" src="/static/'+this.get('pic2')+'" />';
				var img3_1 = '<img class="etalage_thumb_image img-responsive" src="/static/'+this.get('pic3')+'" />';
				var img3_2 = '<img class="etalage_source_image img-responsive" src="/static/'+this.get('pic3')+'" />';
				var img4_1 = '<img class="etalage_thumb_image img-responsive" src="/static/'+this.get('pic4')+'" />';
				var img4_2 = '<img class="etalage_source_image img-responsive" src="/static/'+this.get('pic4')+'" />';
				var li1='<li>'+img1_1+img1_2+'</li>';
				var li2='<li>'+img2_1+img2_2+'</li>';
				var li3='<li>'+img3_1+img3_2+'</li>';
//				var li4='<li>'+img4_1+img4_2+'</li>';
				target.html(li1+li2+li3);
			},
			setCoverImg:function(target){
				var img = '<li><img src="/static/'+this.get('pic5')+'" class="img-responsive"/></li>';
				target.html(img);
			},
			setProductName:function(target){
				var name=this.get('name');
				target.text(name);
				//设置超链接文本
				$('#intro_link').text(name+'简介');
			},
			setProductPrice:function(target){
				var price=this.get('price_low')+'<a href="#">元起，我要讲价</a>';
				target.html(price);
			},
			setBriefIntro:function(target){
				var brief = this.get('brief_intro');
				target.html(brief);
			},
			setRaiseMethod:function(target){
				var raise_method = this.get('raise_method');
				if (raise_method==null||raise_method.replace(/(^s*)|(s*$)/g, "").length ==0){
					target.text('无');
				}else{
					target.text(raise_method);
				}
			},
			setUseMethod:function(target){
				var use_method = this.get('use_method');
				if (use_method==null||use_method.replace(/(^s*)|(s*$)/g, "").length ==0){
					target.text('无');
				}else{
					target.text(use_method);
				}
			},
			setRemarks:function(target){
				var remarks = this.get('remarks');
				if (remarks==null||remarks.replace(/(^s*)|(s*$)/g, "").length ==0){
					target.text('无');
				}else{
					target.html(remarks);
				}
			}
	}
	//本应从服务器读取的，但django在页面加载时已经返回了数据，不用再单独请求，
	//所以将已经随页面加载时返回的数据serverdata直接传进来
	var _initData = function(that,product,intro){
		that.set('productObj',product);
		that.set('name',product['name']);
		that.set('price_low',product['price_low']);
		that.set('pic1',product['pic1']);
		that.set('pic2',product['pic2']);
		that.set('pic3',product['pic3']);
		that.set('pic4',product['pic4']);
		that.set('pic5',product['pic5']);
		that.set('remarks',product['remarks']);
		
		that.set('brief_intro',intro['brief_intro']);
		that.set('raise_method',intro['raise_method']);
		that.set('use_method',intro['use_method']);
	}
	return detail;
})(product_server,intro_server);