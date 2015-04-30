<!DOCTYPE html>
<html lang="en">

<head>
	<noscript><meta http-equiv="refresh" content="0; URL=/files/bun/F04LGDKJM/h52vast.py?nojsmode=1" /></noscript>
<script type="text/javascript">
window.load_start_ms = new Date().getTime();
window.load_log = [];
window.logLoad = function(k) {
	var ms = new Date().getTime();
	window.load_log.push({
		k: k,
		t: (ms-window.load_start_ms)/1000
	})
}
if(self!==top)window.document.write("\u003Cstyle>body * {display:none !important;}\u003C\/style>\u003Ca href=\"#\" onclick="+
"\"top.location.href=window.location.href\" style=\"display:block !important;padding:10px\">Go to Slack.com\u003C\/a>");
</script>


<script type="text/javascript">
window.callSlackAPIUnauthed = function(method, args, callback) {
	var url = '/api/'+method+'?t='+new Date().getTime();
	var req = new XMLHttpRequest();
	
	req.onreadystatechange = function() {
		if (req.readyState == 4) {
			req.onreadystatechange = null;
			var obj;
			
			if (req.status == 200) {
				if (req.responseText.indexOf('{') == 0) {
					try {
						eval('obj = '+req.responseText);
					} catch (err) {
						console.warn('unable to do anything with api rsp');
					}
				}
			}
			
			obj = obj || {
				ok: false	
			}
			
			callback(obj.ok, obj, args);
		}
	}
	
	req.open('POST', url, 1);
	req.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');

	var args2 = [];
	for (i in args) {
		args2[args2.length] = encodeURIComponent(i)+'='+encodeURIComponent(args[i]);
	}

	req.send(args2.join('&'));
}
</script>
			<meta name="referrer" content="no-referrer">
			<meta name="superfish" content="nofish">
	<script type="text/javascript">



var TS_last_log_date = null;
var TSMakeLogDate = function() {
	var date = new Date();

	var y = date.getFullYear();
	var mo = date.getMonth()+1;
	var d = date.getDate();

	var time = {
	  h: date.getHours(),
	  mi: date.getMinutes(),
	  s: date.getSeconds(),
	  ms: date.getMilliseconds()
	};

	Object.keys(time).map(function(moment, index) {
		if(time[moment] < 10) {
			time[moment] = '0' + time[moment];
		}
	});

	var str = y + '/' + mo + '/' + d + ' ' + time.h + ':' + time.mi + ':' + time.s + '.' + time.ms;
	if (TS_last_log_date) {
		var diff = date-TS_last_log_date;
		//str+= ' ('+diff+'ms)';
	}
	TS_last_log_date = date;
	return str+' ';
}

var TSSSB = {
	

	call: function() {
		return false;
	}

	
}

</script>	<script type="text/javascript">TSSSB.call('didFinishLoading');</script>
	    <meta charset="utf-8">
    <title>h52vast.py | EyeWire Slack</title>
    <meta name="author" content="Slack">

								
															
    									
		
		<!-- output_css "core" -->
    <link href="https://slack.global.ssl.fastly.net/3ddf2/style/rollup-plastic.css" rel="stylesheet" type="text/css">

	<!-- output_css "regular" -->
    <link href="https://slack.global.ssl.fastly.net/928c/style/comments.css" rel="stylesheet" type="text/css">
    <link href="https://slack.global.ssl.fastly.net/9a38/style/stars.css" rel="stylesheet" type="text/css">
    <link href="https://slack.global.ssl.fastly.net/f52c/style/print.css" rel="stylesheet" type="text/css">
    <link href="https://slack.global.ssl.fastly.net/53ac/style/files.css" rel="stylesheet" type="text/css">
    <link href="https://slack.global.ssl.fastly.net/7e36/style/libs/codemirror.css" rel="stylesheet" type="text/css">
    <link href="https://slack.global.ssl.fastly.net/5319/style/libs/lato-1.css" rel="stylesheet" type="text/css">

	

	
	
	

	<!--[if lt IE 9]>
	<script src="https://slack.global.ssl.fastly.net/ef0d/js/libs/html5shiv.js"></script>
	<![endif]-->

	
<link id="favicon" rel="shortcut icon" href="https://slack.global.ssl.fastly.net/272a/img/icons/favicon-32.png" sizes="16x16 32x32 48x48" type="image/png" />

<link rel="icon" href="https://slack.global.ssl.fastly.net/ba3c/img/icons/app-256.png" sizes="256x256" type="image/png" />

<link rel="apple-touch-icon-precomposed" sizes="152x152" href="https://slack.global.ssl.fastly.net/0dc1/img/icons/ios-152.png" />
<link rel="apple-touch-icon-precomposed" sizes="144x144" href="https://slack.global.ssl.fastly.net/0dc1/img/icons/ios-144.png" />
<link rel="apple-touch-icon-precomposed" sizes="120x120" href="https://slack.global.ssl.fastly.net/0dc1/img/icons/ios-120.png" />
<link rel="apple-touch-icon-precomposed" sizes="114x114" href="https://slack.global.ssl.fastly.net/0dc1/img/icons/ios-114.png" />
<link rel="apple-touch-icon-precomposed" sizes="72x72" href="https://slack.global.ssl.fastly.net/0dc1/img/icons/ios-72.png" />
<link rel="apple-touch-icon-precomposed" href="https://slack.global.ssl.fastly.net/0dc1/img/icons/ios-57.png" />

<meta name="msapplication-TileColor" content="#FFFFFF" />
<meta name="msapplication-TileImage" content="https://slack.global.ssl.fastly.net/272a/img/icons/app-144.png" />	<script>
!function(a,b){function c(a,b){try{if("function"!=typeof a)return a;if(!a.bugsnag){var c=e();a.bugsnag=function(d){if(b&&b.eventHandler&&(u=d),v=c,!y){var e=a.apply(this,arguments);return v=null,e}try{return a.apply(this,arguments)}catch(f){throw l("autoNotify",!0)&&(x.notifyException(f,null,null,"error"),s()),f}finally{v=null}},a.bugsnag.bugsnag=a.bugsnag}return a.bugsnag}catch(d){return a}}function d(){B=!1}function e(){var a=document.currentScript||v;if(!a&&B){var b=document.scripts||document.getElementsByTagName("script");a=b[b.length-1]}return a}function f(a){var b=e();b&&(a.script={src:b.src,content:l("inlineScript",!0)?b.innerHTML:""})}function g(b){var c=l("disableLog"),d=a.console;void 0===d||void 0===d.log||c||d.log("[Bugsnag] "+b)}function h(b,c,d){if(d>=5)return encodeURIComponent(c)+"=[RECURSIVE]";d=d+1||1;try{if(a.Node&&b instanceof a.Node)return encodeURIComponent(c)+"="+encodeURIComponent(r(b));var e=[];for(var f in b)if(b.hasOwnProperty(f)&&null!=f&&null!=b[f]){var g=c?c+"["+f+"]":f,i=b[f];e.push("object"==typeof i?h(i,g,d):encodeURIComponent(g)+"="+encodeURIComponent(i))}return e.join("&")}catch(j){return encodeURIComponent(c)+"="+encodeURIComponent(""+j)}}function i(a,b){if(null==b)return a;a=a||{};for(var c in b)if(b.hasOwnProperty(c))try{a[c]=b[c].constructor===Object?i(a[c],b[c]):b[c]}catch(d){a[c]=b[c]}return a}function j(a,b){a+="?"+h(b)+"&ct=img&cb="+(new Date).getTime();var c=new Image;c.src=a}function k(a){var b={},c=/^data\-([\w\-]+)$/;if(a)for(var d=a.attributes,e=0;e<d.length;e++){var f=d[e];if(c.test(f.nodeName)){var g=f.nodeName.match(c)[1];b[g]=f.value||f.nodeValue}}return b}function l(a,b){C=C||k(J);var c=void 0!==x[a]?x[a]:C[a.toLowerCase()];return"false"===c&&(c=!1),void 0!==c?c:b}function m(a){return a&&a.match(D)?!0:(g("Invalid API key '"+a+"'"),!1)}function n(b,c){var d=l("apiKey");if(m(d)&&A){A-=1;var e=l("releaseStage"),f=l("notifyReleaseStages");if(f){for(var h=!1,k=0;k<f.length;k++)if(e===f[k]){h=!0;break}if(!h)return}var n=[b.name,b.message,b.stacktrace].join("|");if(n!==w){w=n,u&&(c=c||{},c["Last Event"]=q(u));var o={notifierVersion:H,apiKey:d,projectRoot:l("projectRoot")||a.location.protocol+"//"+a.location.host,context:l("context")||a.location.pathname,userId:l("userId"),user:l("user"),metaData:i(i({},l("metaData")),c),releaseStage:e,appVersion:l("appVersion"),url:a.location.href,userAgent:navigator.userAgent,language:navigator.language||navigator.userLanguage,severity:b.severity,name:b.name,message:b.message,stacktrace:b.stacktrace,file:b.file,lineNumber:b.lineNumber,columnNumber:b.columnNumber,payloadVersion:"2"},p=x.beforeNotify;if("function"==typeof p){var r=p(o,o.metaData);if(r===!1)return}return 0===o.lineNumber&&/Script error\.?/.test(o.message)?g("Ignoring cross-domain script error. See https://bugsnag.com/docs/notifiers/js/cors"):(j(l("endpoint")||G,o),void 0)}}}function o(){var a,b,c=10,d="[anonymous]";try{throw new Error("")}catch(e){a="<generated>\n",b=p(e)}if(!b){a="<generated-ie>\n";var f=[];try{for(var h=arguments.callee.caller.caller;h&&f.length<c;){var i=E.test(h.toString())?RegExp.$1||d:d;f.push(i),h=h.caller}}catch(j){g(j)}b=f.join("\n")}return a+b}function p(a){return a.stack||a.backtrace||a.stacktrace}function q(a){var b={millisecondsAgo:new Date-a.timeStamp,type:a.type,which:a.which,target:r(a.target)};return b}function r(a){if(a){var b=a.attributes;if(b){for(var c="<"+a.nodeName.toLowerCase(),d=0;d<b.length;d++)b[d].value&&"null"!=b[d].value.toString()&&(c+=" "+b[d].name+'="'+b[d].value+'"');return c+">"}return a.nodeName}}function s(){z+=1,a.setTimeout(function(){z-=1})}function t(a,b,c){var d=a[b],e=c(d);a[b]=e}var u,v,w,x={},y=!0,z=0,A=10;x.noConflict=function(){return a.Bugsnag=b,x},x.refresh=function(){A=10},x.notifyException=function(a,b,c,d){b&&"string"!=typeof b&&(c=b,b=void 0),c||(c={}),f(c),n({name:b||a.name,message:a.message||a.description,stacktrace:p(a)||o(),file:a.fileName||a.sourceURL,lineNumber:a.lineNumber||a.line,columnNumber:a.columnNumber?a.columnNumber+1:void 0,severity:d||"warning"},c)},x.notify=function(b,c,d,e){n({name:b,message:c,stacktrace:o(),file:a.location.toString(),lineNumber:1,severity:e||"warning"},d)};var B="complete"!==document.readyState;document.addEventListener?(document.addEventListener("DOMContentLoaded",d,!0),a.addEventListener("load",d,!0)):a.attachEvent("onload",d);var C,D=/^[0-9a-f]{32}$/i,E=/function\s*([\w\-$]+)?\s*\(/i,F="https://notify.bugsnag.com/",G=F+"js",H="2.4.7",I=document.getElementsByTagName("script"),J=I[I.length-1];if(a.atob){if(a.ErrorEvent)try{0===new a.ErrorEvent("test").colno&&(y=!1)}catch(K){}}else y=!1;if(l("autoNotify",!0)){t(a,"onerror",function(b){return function(c,d,e,g,h){var i=l("autoNotify",!0),j={};!g&&a.event&&(g=a.event.errorCharacter),f(j),v=null,i&&!z&&n({name:h&&h.name||"window.onerror",message:c,file:d,lineNumber:e,columnNumber:g,stacktrace:h&&p(h)||o(),severity:"error"},j),b&&b(c,d,e,g,h)}});var L=function(a){return function(b,d){if("function"==typeof b){b=c(b);var e=Array.prototype.slice.call(arguments,2);return a(function(){b.apply(this,e)},d)}return a(b,d)}};t(a,"setTimeout",L),t(a,"setInterval",L),a.requestAnimationFrame&&t(a,"requestAnimationFrame",function(a){return function(b){return a(c(b))}}),a.setImmediate&&t(a,"setImmediate",function(a){return function(){var b=Array.prototype.slice.call(arguments);return b[0]=c(b[0]),a.apply(this,b)}}),"EventTarget Window Node ApplicationCache AudioTrackList ChannelMergerNode CryptoOperation EventSource FileReader HTMLUnknownElement IDBDatabase IDBRequest IDBTransaction KeyOperation MediaController MessagePort ModalWindow Notification SVGElementInstance Screen TextTrack TextTrackCue TextTrackList WebSocket WebSocketWorker Worker XMLHttpRequest XMLHttpRequestEventTarget XMLHttpRequestUpload".replace(/\w+/g,function(b){var d=a[b]&&a[b].prototype;d&&d.hasOwnProperty&&d.hasOwnProperty("addEventListener")&&(t(d,"addEventListener",function(a){return function(b,d,e,f){return d&&d.handleEvent&&(d.handleEvent=c(d.handleEvent,{eventHandler:!0})),a.call(this,b,c(d,{eventHandler:!0}),e,f)}}),t(d,"removeEventListener",function(a){return function(b,d,e,f){return a.call(this,b,d,e,f),a.call(this,b,c(d),e,f)}}))})}a.Bugsnag=x,"function"==typeof define&&define.amd?define([],function(){return x}):"object"==typeof module&&"object"==typeof module.exports&&(module.exports=x)}(window,window.Bugsnag);
Bugsnag.apiKey = "2a86b308af5a81d2c9329fedfb4b30c7";
Bugsnag.appVersion = "76609d9e04fa84ae39a5e2468b2f6f61492dac29-1430405258";
Bugsnag.endpoint = "https://errors.slack-core.com/js";
Bugsnag.releaseStage = "prod";
Bugsnag.user = {id:"U034A3B71",name:"jingpeng",email:"jingpeng@princeton.edu"};
Bugsnag.metaData = {};
Bugsnag.metaData.team = {id:"T02FH1DRA",name:"EyeWire",domain:"eyewire"};
Bugsnag.refresh_interval = setInterval(function () { (window.TS && window.TS.client) ? Bugsnag.refresh() : clearInterval(Bugsnag.refresh_interval); }, 15 * 60 * 1000);
</script>			<script type="text/javascript">

	(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
	(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
	m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
	})(window,document,'script','//www.google-analytics.com/analytics.js','ga');
	ga('create', 'UA-106458-17', 'slack.com');
	ga('send', 'pageview');


	(function(e,c,b,f,d,g,a){e.SlackBeaconObject=d;
	e[d]=e[d]||function(){(e[d].q=e[d].q||[]).push([1*new Date(),arguments])};
	e[d].l=1*new Date();g=c.createElement(b);a=c.getElementsByTagName(b)[0];
	g.async=1;g.src=f;a.parentNode.insertBefore(g,a)
	})(window,document,"script","https://slack.global.ssl.fastly.net/dcf8/js/libs/beacon.js","sb");
	sb('set', 'token', '3307f436963e02d4f9eb85ce5159744c');
	sb('set', 'user_id', 'U034A3B71');
	sb('set', 'user_batch', "referred-launch");
	sb('set', 'user_created', "2014-12-04");
	sb('set', 'name_tag', 'eyewire/jingpeng');
	sb('track', 'pageview');

	function track(a){ga('send','event','web',a);sb('track',a);}


	
	(function(f,b){if(!b.__SV){var a,e,i,g;window.mixpanel=b;b._i=[];b.init=function(a,e,d){function f(b,h){var a=h.split(".");2==a.length&&(b=b[a[0]],h=a[1]);b[h]=function(){b.push([h].concat(Array.prototype.slice.call(arguments,0)))}}var c=b;"undefined"!==typeof d?c=b[d]=[]:d="mixpanel";c.people=c.people||[];c.toString=function(b){var a="mixpanel";"mixpanel"!==d&&(a+="."+d);b||(a+=" (stub)");return a};c.people.toString=function(){return c.toString(1)+".people (stub)"};i="disable track track_pageview track_links track_forms register register_once alias unregister identify name_tag set_config people.set people.set_once people.increment people.append people.track_charge people.clear_charges people.delete_user".split(" ");
	for(g=0;g<i.length;g++)f(c,i[g]);b._i.push([a,e,d])};b.__SV=1.2;a=f.createElement("script");a.type="text/javascript";a.async=!0;a.src="//cdn.mxpnl.com/libs/mixpanel-2-latest.min.js";e=f.getElementsByTagName("script")[0];e.parentNode.insertBefore(a,e)}})(document,window.mixpanel||[]);
	
	mixpanel.init("12d52d8633a5b432975592d13ebd3f34");

	function mixpanel_track(event_name){if(window.mixpanel&&event_name)mixpanel.track(event_name);}

</script>	
</head>

  <body >

		  			<script>
		
			var w = Math.max(document.documentElement.clientWidth, window.innerWidth || 0);
			if (w > 1440) document.querySelector('body').classList.add('widescreen');
		
		</script>
	
  	
	

			<nav id="site_nav" class="no_transition">

	<div id="site_nav_contents">

		<div id="user_menu">
			<div id="user_menu_contents">
				<div id="user_menu_avatar">
										<span class="member_image thumb_48" style="background-image: url('https://secure.gravatar.com/avatar/6e3c17d7fd502ce0426b632be329381b.jpg?s=192&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0001.png')" data-thumb-size="48" data-member-id="U034A3B71"></span>
					<span class="member_image thumb_36" style="background-image: url('https://secure.gravatar.com/avatar/6e3c17d7fd502ce0426b632be329381b.jpg?s=72&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0001-72.png')" data-thumb-size="36" data-member-id="U034A3B71"></span>
				</div>
				<h3>Signed in as</h3>
				<span id="user_menu_name">jingpeng</span>
			</div>
		</div>

		<div class="nav_contents">

			<ul class="primary_nav">
				<li><a href="/home"><i class="fa fa-home"></i>Home</a></li>
				<li><a href="/account"><i class="fa fa-user"></i>Account & Profile</a></li>
				<li><a href="/services/new"><i class="fa fa-wrench"></i>Integrations</a></li>
				<li><a href="/archives"><i class="fa fa-inbox"></i>Message Archives</a></li>
				<li><a href="/files"><i class="fa fa-file"></i>Files</a></li>
				<li><a href="/team"><i class="fa fa-book"></i>Team Directory</a></li>
									<li><a href="/stats"><i class="fa fa-tachometer"></i>Statistics</a></li>
													<li><a href="/customize"><i class="fa fa-magic"></i>Customize</a></li>
													<li><a href="/account/team"><i class="fa fa-cog"></i>Team Settings</a></li>
							</ul>

			
		</div>

		<div id="footer">

			<ul id="footer_nav">
				<li><a href="/is">Tour</a></li>
				<li><a href="/apps">Apps</a></li>
				<li><a href="/brand-guidelines">Brand Guidelines</a></li>
				<li><a href="/help">Help</a></li>
				<li><a href="https://api.slack.com" target="_blank">API<i class="fa fa-external-link small_left_margin"></i></a></li>
								<li><a href="/pricing">Pricing</a></li>
				<li><a href="/help/requests/new">Contact</a></li>
				<li><a href="/terms-of-service">Policies</a></li>
				<li><a href="http://slackhq.com/" target="_blank">Our Blog</a></li>
				<li><a href="https://slack.com/signout/2527047860?crumb=s-1430407044-52addd2a93-%E2%98%83">Sign Out<i class="fa fa-sign-out small_left_margin"></i></a></li>
			</ul>

			<p id="footer_signature">Made with <i class="fa fa-heart"></i> by Slack</p>

		</div>

	</div>
</nav>	
			<header>
							<a id="menu_toggle" class="no_transition">
					<span class="menu_icon"></span>
					<span class="menu_label">Menu</span>
					<span class="vert_divider"></span>
				</a>
				<h1 id="header_team_name" class="inline_block no_transition">
					<a href="/home">
						<i class="fa fa-home" /></i>
						EyeWire
					</a>
				</h1>
				<div class="header_nav">
					<div class="header_btns float_right">
						<a id="team_switcher">
							<i class="fa fa-th-large"></i>
							<span class="block label">Teams</span>
						</a>
						<a href="/help" id="help_link">
							<i class="fa fa-life-ring"></i>
							<span class="block label">Help</span>
						</a>
						<a href="/messages">
							<img src="https://slack.global.ssl.fastly.net/0dc1/img/icons/ios-64.png" srcset="https://slack.global.ssl.fastly.net/0dc1/img/icons/ios-32.png 1x, https://slack.global.ssl.fastly.net/0dc1/img/icons/ios-64.png 2x" />
							<span class="block label">Launch</span>
						</a>
					</div>
								                    <ul id="header_team_nav">
			                        			                            <li class="active">
			                            	<a href="https://eyewire.slack.com/home" target="https://eyewire.slack.com/">
			                            					                            			<i class="fa fa-check active_icon"></i>
			                            					                            						                            		<i class="team_icon" style="background-image: url('https://s3-us-west-2.amazonaws.com/slack-files2/avatars/2014-11-21/3062828575_f1574217221993963db1_44.jpg');"></i>
				                            				                            		<span class="switcher_label team_name">EyeWire</span>
			                            	</a>
			                            </li>
			                        			                        <li id="add_team_option"><a href="https://slack.com/signin" target="_blank"><i class="fa fa-plus team_icon"></i> <span class="switcher_label">Sign in to another team...</span></a></li>
			                    </ul>
			                				</div>
			
			
		</header>
	
	<div id="page">

		<div id="page_contents" >

<p class="print_only">
	<strong>Created by bun on April 30, 2015 at 11:16 AM</strong><br />
	<span class="subtle_silver break_word">https://eyewire.slack.com/files/bun/F04LGDKJM/h52vast.py</span>
</p>

<div class="file_header_container no_print"></div>

<div class="alert_container">
		<div class="file_public_link_shared alert" style="display: none;">
		
	<i class="fa fa-link"></i> Public Link: <a class="file_public_link" href="https://slack-files.com/T02FH1DRA-F04LGDKJM-25f41f59ca" target="new">https://slack-files.com/T02FH1DRA-F04LGDKJM-25f41f59ca</a>
</div></div>

<div id="file_page" class="card top_padding">

	<p class="small subtle_silver no_print meta">
		855b Python snippet created on <span class="date">April 30th 2015</span>.
		This file is private.		<span class="file_share_list"></span>
	</p>

	<a id="file_action_cog" class="action_cog action_cog_snippet float_right no_print">
		<span>Actions </span><i class="fa fa-cog"></i>
	</a>
	<a id="snippet_expand_toggle" class="float_right no_print">
		<i class="fa fa-expand "></i>
		<i class="fa fa-compress hidden"></i>
	</a>

	<div class="large_bottom_margin clearfix">
		<pre id="file_contents"># -*- coding: utf-8 -*-
&quot;&quot;&quot;
Created on Wed Mar 11 16:18:34 2015

@author: jingpeng
&quot;&quot;&quot;
#%% parameters
import numpy as np

Dir = &#039;/usr/people/bds2/seungmount/Omni/TracerTasks/Piriform_cortex_Corrections/Chunk_07/Chunk_07_EM/&#039;
filename =&#039;chunk_07_em&#039;
tifname = &#039;chunk_07_em.tif&#039;

isgray = True

#%% read the data
import h5py
f = h5py.File(Dir + filename )
invol = np.asarray(f[&#039;/main&#039;])
f.close()

if isgray:
	outvol = (invol-invol.min()) / (invol.max()-invol.min()) * 255
	outvol = outvol.astype(&#039;uint8&#039;)
else:
	vol = np.asarray(invol* ((2**24-1)/float(invol.max())), dtype=&#039;uint32&#039;) 
	rgb = np.zeros( np.append(np.array( invol.shape ), 3), dtype=&#039;uint8&#039;)

	rgb[:,:,:, 0] = np.remainder( invol, 256)
	rgb[:,:,:, 1] = np.remainder( invol, 25536) / 256
	rgb[:,:,:, 2] = invol / 25536

#%% write as tiff
import tifffile
tifffile.imsave(Dir + tifname, outvol)
</pre>

		<p class="file_page_meta no_print" style="line-height: 1.5rem;">
			<label class="checkbox normal mini float_right no_top_padding no_min_width">
				<input type="checkbox" id="file_preview_wrap_cb"> wrap long lines
			</label>
		</p>

	</div>

	<div id="comments_holder" class="clearfix clear_both">
	<div class="col span_1_of_6"></div>
	<div class="col span_4_of_6 no_right_padding">
		<div id="file_page_comments">
					</div>	
		<form action="https://eyewire.slack.com/files/bun/F04LGDKJM/h52vast.py" 
		id="file_comment_form" 
					class="comment_form"
				method="post">
			<a href="/team/jingpeng" class="member_preview_link" data-member-id="U034A3B71" >
			<span class="member_image thumb_36" style="background-image: url('https://secure.gravatar.com/avatar/6e3c17d7fd502ce0426b632be329381b.jpg?s=72&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0001-72.png')" data-thumb-size="36" data-member-id="U034A3B71"></span>
		</a>		
		<input type="hidden" name="addcomment" value="1" />
	<input type="hidden" name="crumb" value="s-1430407044-4c81b5630d-☃" />

	<textarea id="file_comment" data-el-id-to-keep-in-view="file_comment_submit_btn" class="comment_input small_bottom_margin" name="comment" wrap="virtual" ></textarea>
	<span class="input_note float_left cloud_silver file_comment_tip">cmd+enter to submit</span>	<button id="file_comment_submit_btn" type="submit" class="btn float_right  ladda-button" data-style="expand-right"><span class="ladda-label">Add Comment</span></button>
</form>

<form action="https://eyewire.slack.com/files/bun/F04LGDKJM/h52vast.py" 
		id="file_edit_comment_form" 
					class="edit_comment_form hidden"
				method="post">
	<textarea id="file_edit_comment" class="comment_input small_bottom_margin" name="comment" wrap="virtual"></textarea><br>
	<span class="input_note float_left cloud_silver file_comment_tip">cmd+enter to submit</span>	<input type="submit" class="save btn float_right " value="Save Changes" />
	<button class="cancel btn btn_outline float_right small_right_margin ">Cancel</button>
</form>	
	</div>
	<div class="col span_1_of_6"></div>
</div>
</div>

	

		
	</div>
	<div id="overlay"></div>
</div>




<script type="text/javascript">
var cdn_url = 'https://slack.global.ssl.fastly.net';
</script>
			<script type="text/javascript">
<!--
	// common boot_data
	var boot_data = {
		start_ms: new Date().getTime(),
		app: 'web',
		is_mobile: false,
		user_id: 'U034A3B71',
		version_ts: '1430405258',
		version_uid: '76609d9e04fa84ae39a5e2468b2f6f61492dac29',
		redir_domain: 'slack-redir.net',
		api_url: '/api/',
		team_url: 'https://eyewire.slack.com/',
		image_proxy_url: 'https://slack-imgs.com/',
		api_token: 'xoxs-2527047860-3146113239-3768073610-03d50b5485',

		feature_status: false,
		feature_search_attachments: false,
		feature_archive_viewer: true,

		feature_reactions: false,
		feature_spaces: false,
		feature_a11y_keyboard_shortcuts: false,
		feature_email_integration: false,
		feature_email_ingestion: false,
		feature_attachments_inline: false,
		feature_cmd_autocomplete: true,
		feature_ms_on_space: true,
		feature_flexpane_rework: true,
		feature_fix_files: false,
		feature_chat_sounds: false,
		feature_require_at: true,
		feature_image_proxy: true,
		feature_channel_eventlog_client: true,
		feature_bot_users: true,
		feature_muting: true,
		feature_macssb1_banner: true,
		feature_winssb1_banner: true,
		feature_latest_event_ts: true,
		feature_no_redirects_in_ssb: true,
		feature_referer_policy: true,
		feature_client_exif_orientation_on_uploads: true,
		feature_lato_fonts: true,
		feature_at_channel_warning: true,
		feature_at_channel_warning_non_admin_message: true,
		feature_pins: true,
		feature_join_leave_rollups: true,
		feature_bot_message_label: true,
		feature_oldest_msg_storing: true,
		feature_new_btns_in_channel_list: true,
		feature_box_plugin: true,
		feature_post_previews: false,
		feature_pricing_page_refresh: false,
		feature_client_date_formatting: false,
		feature_more_field_in_message_attachments: false,
		feature_user_hidden_msgs: false,
		feature_prompt_to_share: false,
		feature_file_url_private_conversion: false,
		feature_spaces_in_windows: false,
		feature_screenhero: false,
		feature_msg_input_revisions: false,
		feature_combined_menu: false,
		feature_lazy_load_pins: true,

		img: {
			app_icon: 'https://slack.global.ssl.fastly.net/272a/img/slack_growl_icon.png'
		},
		page_needs_custom_emoji: false
	};



	// client boot data
			boot_data.login_data = JSON.parse('{\"ok\":true,\"self\":{\"id\":\"U034A3B71\",\"name\":\"jingpeng\",\"prefs\":{\"highlight_words\":\"\",\"user_colors\":\"\",\"color_names_in_list\":true,\"growls_enabled\":true,\"tz\":\"America\\/Indiana\\/Indianapolis\",\"push_dm_alert\":true,\"push_mention_alert\":true,\"push_everything\":false,\"push_idle_wait\":2,\"push_sound\":\"b2.mp3\",\"push_loud_channels\":\"\",\"push_mention_channels\":\"\",\"push_loud_channels_set\":\"C033T5AGA,C02TC3VDY,C03CKSG47\",\"email_alerts\":\"none\",\"email_alerts_sleep_until\":0,\"email_misc\":true,\"email_weekly\":true,\"welcome_message_hidden\":false,\"all_channels_loud\":false,\"loud_channels\":\"\",\"never_channels\":\"C033T5AGA,C02TC3VDY\",\"loud_channels_set\":\"C033T5AGA,C02TC3VDY\",\"show_member_presence\":true,\"search_sort\":\"timestamp\",\"expand_inline_imgs\":true,\"expand_internal_inline_imgs\":true,\"expand_snippets\":false,\"posts_formatting_guide\":true,\"seen_welcome_2\":true,\"seen_ssb_prompt\":false,\"search_only_my_channels\":false,\"emoji_mode\":\"default\",\"emoji_use\":\"{\\\"grinning\\\":1,\\\"simple_smile\\\":6,\\\"rocket\\\":1}\",\"has_invited\":false,\"has_uploaded\":true,\"has_created_channel\":true,\"search_exclude_channels\":\"\",\"messages_theme\":\"default\",\"webapp_spellcheck\":true,\"no_joined_overlays\":true,\"no_created_overlays\":false,\"dropbox_enabled\":false,\"seen_user_menu_tip_card\":true,\"seen_team_menu_tip_card\":true,\"seen_channel_menu_tip_card\":true,\"seen_message_input_tip_card\":true,\"seen_channels_tip_card\":true,\"seen_domain_invite_reminder\":false,\"seen_member_invite_reminder\":false,\"seen_flexpane_tip_card\":true,\"seen_search_input_tip_card\":true,\"mute_sounds\":false,\"arrow_history\":false,\"tab_ui_return_selects\":true,\"obey_inline_img_limit\":true,\"new_msg_snd\":\"knock_brush.mp3\",\"collapsible\":false,\"collapsible_by_click\":true,\"require_at\":true,\"mac_ssb_bounce\":\"\",\"mac_ssb_bullet\":true,\"expand_non_media_attachments\":true,\"show_typing\":true,\"pagekeys_handled\":true,\"last_snippet_type\":\"python\",\"display_real_names_override\":0,\"time24\":false,\"enter_is_special_in_tbt\":false,\"graphic_emoticons\":false,\"convert_emoticons\":true,\"autoplay_chat_sounds\":true,\"ss_emojis\":true,\"sidebar_behavior\":\"\",\"mark_msgs_read_immediately\":true,\"start_scroll_at_oldest\":true,\"snippet_editor_wrap_long_lines\":false,\"ls_disabled\":false,\"sidebar_theme\":\"default\",\"sidebar_theme_custom_values\":\"\",\"f_key_search\":false,\"k_key_omnibox\":true,\"speak_growls\":false,\"mac_speak_voice\":\"com.apple.speech.synthesis.voice.Alex\",\"mac_speak_speed\":250,\"comma_key_prefs\":false,\"at_channel_suppressed_channels\":\"\",\"push_at_channel_suppressed_channels\":\"\",\"prompted_for_email_disabling\":false,\"full_text_extracts\":false,\"no_text_in_notifications\":false,\"muted_channels\":\"C033T5AGA,C02TC3VDY,C03CKSG47,C03424R9S\",\"no_macssb1_banner\":false,\"no_winssb1_banner\":false,\"privacy_policy_seen\":true,\"search_exclude_bots\":false,\"fuzzy_matching\":false,\"load_lato_2\":false,\"fuller_timestamps\":false,\"last_seen_at_channel_warning\":0,\"enable_flexpane_rework\":false,\"flex_resize_window\":false,\"msg_preview\":false,\"msg_preview_displaces\":true,\"msg_preview_persistent\":true,\"emoji_autocomplete_big\":false,\"winssb_run_from_tray\":true,\"two_factor_auth_enabled\":false,\"mentions_exclude_at_channels\":true,\"box_enabled\":false},\"created\":1417723049},\"team\":{\"id\":\"T02FH1DRA\",\"name\":\"EyeWire\",\"email_domain\":\"eyewire.org,mit.edu,princeton.edu\",\"domain\":\"eyewire\",\"msg_edit_window_mins\":-1,\"prefs\":{\"default_channels\":[\"C02FH1DRJ\",\"C02FH1DRL\"],\"msg_edit_window_mins\":-1,\"allow_message_deletion\":true,\"hide_referers\":true,\"display_real_names\":false,\"who_can_at_everyone\":\"regular\",\"who_can_at_channel\":\"ra\",\"warn_before_at_channel\":\"always\",\"who_can_create_channels\":\"regular\",\"who_can_archive_channels\":\"regular\",\"who_can_create_groups\":\"ra\",\"who_can_post_general\":\"ra\",\"who_can_kick_channels\":\"admin\",\"who_can_kick_groups\":\"regular\",\"retention_type\":0,\"retention_duration\":0,\"group_retention_type\":0,\"group_retention_duration\":0,\"dm_retention_type\":0,\"dm_retention_duration\":0,\"require_at_for_mention\":0,\"compliance_export_start\":0},\"icon\":{\"image_34\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2014-11-21\\/3062828575_f1574217221993963db1_34.jpg\",\"image_44\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2014-11-21\\/3062828575_f1574217221993963db1_44.jpg\",\"image_68\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2014-11-21\\/3062828575_f1574217221993963db1_44.jpg\",\"image_88\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2014-11-21\\/3062828575_f1574217221993963db1_44.jpg\",\"image_102\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2014-11-21\\/3062828575_f1574217221993963db1_44.jpg\",\"image_132\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2014-11-21\\/3062828575_f1574217221993963db1_44.jpg\",\"image_original\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2014-11-21\\/3062828575_f1574217221993963db1_original.jpg\"},\"over_storage_limit\":false,\"plan\":\"std\"},\"latest_event_ts\":\"1430406444.000000\",\"channels\":[{\"id\":\"C02TC34RG\",\"name\":\"accuracy\",\"is_channel\":true,\"created\":1415060842,\"creator\":\"U02T22LS0\",\"is_archived\":false,\"is_general\":false,\"has_pins\":false,\"is_member\":false},{\"id\":\"C03C9U556\",\"name\":\"alignment\",\"is_channel\":true,\"created\":1421293649,\"creator\":\"U02TVGRF6\",\"is_archived\":false,\"is_general\":false,\"has_pins\":false,\"is_member\":true,\"members\":[\"U02FH1DRC\",\"U02TC3ELE\",\"U02TTRYS7\",\"U02TVGRF6\",\"U02U5UULA\",\"U0320HC20\",\"U03404U57\",\"U03419JM6\",\"U034A3B71\",\"U034REYU6\"],\"topic\":{\"value\":\"\",\"creator\":\"\",\"last_set\":0},\"purpose\":{\"value\":\"image stitching and alignment\",\"creator\":\"U02TVGRF6\",\"last_set\":1421293649}},{\"id\":\"C02TETD0G\",\"name\":\"autostats\",\"is_channel\":true,\"created\":1415101550,\"creator\":\"U02T22LS0\",\"is_archived\":false,\"is_general\":false,\"has_pins\":false,\"is_member\":false},{\"id\":\"C03R89V16\",\"name\":\"aws-pipeline\",\"is_channel\":true,\"created\":1424977956,\"creator\":\"U02T22LS0\",\"is_archived\":false,\"is_general\":false,\"is_starred\":true,\"has_pins\":false,\"is_member\":true,\"members\":[\"U02FH1DRC\",\"U02T22LS0\",\"U02TVGRF6\",\"U02U8RKR3\",\"U03404U57\",\"U03419JM6\",\"U034A3B71\",\"U034REYU6\"],\"topic\":{\"value\":\"\",\"creator\":\"\",\"last_set\":0},\"purpose\":{\"value\":\"Have a pipeline working using AWS\",\"creator\":\"U02T22LS0\",\"last_set\":1424977957}},{\"id\":\"C03447NSA\",\"name\":\"badges\",\"is_channel\":true,\"created\":1417653617,\"creator\":\"U02FH1DRC\",\"is_archived\":false,\"is_general\":false,\"has_pins\":false,\"is_member\":false},{\"id\":\"C03LMD8B9\",\"name\":\"beerclub\",\"is_channel\":true,\"created\":1423758089,\"creator\":\"U02TU0KLR\",\"is_archived\":false,\"is_general\":false,\"has_pins\":false,\"is_member\":true,\"members\":[\"U02T22LS0\",\"U02TTRYS7\",\"U02TU0KLR\",\"U02TVGRF6\",\"U02U8RKR3\",\"U031MU6L7\",\"U033RMUJH\",\"U033T4SHE\",\"U033T5216\",\"U033TB01W\",\"U03419JM6\",\"U034A3B71\",\"U037QLRHE\"],\"topic\":{\"value\":\"\",\"creator\":\"\",\"last_set\":0},\"purpose\":{\"value\":\"to promote productivity, (alcoholic) education, and general well being of seung lab minions\",\"creator\":\"U02TU0KLR\",\"last_set\":1423758089}},{\"id\":\"C038BR6RK\",\"name\":\"blog\",\"is_channel\":true,\"created\":1419386785,\"creator\":\"U033NHWDE\",\"is_archived\":false,\"is_general\":false,\"has_pins\":false,\"is_member\":false},{\"id\":\"C037CRSEQ\",\"name\":\"boston\",\"is_channel\":true,\"created\":1418913800,\"creator\":\"U02FH1DRC\",\"is_archived\":false,\"is_general\":false,\"has_pins\":false,\"is_member\":false},{\"id\":\"C0340KCAV\",\"name\":\"bugs\",\"is_channel\":true,\"created\":1417636934,\"creator\":\"U033PNZ44\",\"is_archived\":false,\"is_general\":false,\"has_pins\":false,\"is_member\":false},{\"id\":\"C034D39AL\",\"name\":\"dec10\",\"is_channel\":true,\"created\":1417733880,\"creator\":\"U02FH1DRC\",\"is_archived\":true,\"is_general\":false,\"has_pins\":false,\"is_member\":false},{\"id\":\"C039JD0DF\",\"name\":\"design\",\"is_channel\":true,\"created\":1420232394,\"creator\":\"U02FH1DRC\",\"is_archived\":false,\"is_general\":false,\"has_pins\":false,\"is_member\":false},{\"id\":\"C044ZNHB2\",\"name\":\"dev-backend_omni\",\"is_channel\":true,\"created\":1427238882,\"creator\":\"U02U8RKR3\",\"is_archived\":false,\"is_general\":false,\"has_pins\":false,\"is_member\":false},{\"id\":\"C02TC3VDY\",\"name\":\"development\",\"is_channel\":true,\"created\":1415061087,\"creator\":\"U02T22LS0\",\"is_archived\":false,\"is_general\":false,\"has_pins\":false,\"is_member\":true,\"members\":[\"U02FH1DRC\",\"U02T22LS0\",\"U02TC3ELE\",\"U02TVGRF6\",\"U02U5UULA\",\"U02U8RKR3\",\"U031MU6L7\",\"U031YCFB8\",\"U0320HC20\",\"U033NHWDE\",\"U033PNZ44\",\"U033TCE0W\",\"U033TSX9A\",\"U03404U57\",\"U03419JM6\",\"U034A3B71\",\"U034REYU6\",\"U03LE2SNL\",\"U03SCFJSV\"],\"topic\":{\"value\":\"\",\"creator\":\"\",\"last_set\":0},\"purpose\":{\"value\":\"A general chat for all related conversations to coding\",\"creator\":\"U02T22LS0\",\"last_set\":1415061087}},{\"id\":\"C0341JD6Y\",\"name\":\"done_cells_bomni\",\"is_channel\":true,\"created\":1417632100,\"creator\":\"U033NHWDE\",\"is_archived\":false,\"is_general\":false,\"has_pins\":false,\"is_member\":false},{\"id\":\"C02TFNZDA\",\"name\":\"done_cells_ew\",\"is_channel\":true,\"created\":1415110809,\"creator\":\"U02T22LS0\",\"is_archived\":false,\"is_general\":false,\"has_pins\":false,\"is_member\":false},{\"id\":\"C03LSQ232\",\"name\":\"edu\",\"is_channel\":true,\"created\":1423775318,\"creator\":\"U02FH1DRC\",\"is_archived\":false,\"is_general\":false,\"has_pins\":false,\"is_member\":false},{\"id\":\"C03424R9S\",\"name\":\"emergency-eyewire\",\"is_channel\":true,\"created\":1417636885,\"creator\":\"U033PNZ44\",\"is_archived\":false,\"is_general\":false,\"has_pins\":false,\"is_member\":true,\"members\":[\"U02FH1DRC\",\"U02T22LS0\",\"U02TC3ELE\",\"U02TVGRF6\",\"U02U5UULA\",\"U02U8RKR3\",\"U031MU6L7\",\"U031YCFB8\",\"U0320HC20\",\"U033NHWDE\",\"U033PNZ44\",\"U033TCE0W\",\"U033TSX9A\",\"U034A3B71\"],\"topic\":{\"value\":\"\",\"creator\":\"\",\"last_set\":0},\"purpose\":{\"value\":\"Is the site down, is HQ on fire? Report it here.  Found a bug?  Use the #bugs channel\",\"creator\":\"U033NHWDE\",\"last_set\":1417709066}},{\"id\":\"C0390Q7PQ\",\"name\":\"ew-featuresuggestions\",\"is_channel\":true,\"created\":1419890180,\"creator\":\"U033TSX9A\",\"is_archived\":false,\"is_general\":false,\"has_pins\":false,\"is_member\":false},{\"id\":\"C03069WGZ\",\"name\":\"eyewire-api\",\"is_channel\":true,\"created\":1415921512,\"creator\":\"U02TC3ELE\",\"is_archived\":false,\"is_general\":false,\"has_pins\":false,\"is_member\":false},{\"id\":\"C031Z8S94\",\"name\":\"eyewire-pointsystem\",\"is_channel\":true,\"created\":1416631020,\"creator\":\"U02TC3ELE\",\"is_archived\":false,\"is_general\":false,\"has_pins\":false,\"is_member\":false},{\"id\":\"C02FH1DRJ\",\"name\":\"general\",\"is_channel\":true,\"created\":1407542311,\"creator\":\"U02FH1DRC\",\"is_archived\":false,\"is_general\":true,\"has_pins\":false,\"is_member\":true,\"members\":[\"U02FH1DRC\",\"U02FH4TGY\",\"U02T22LS0\",\"U02TC3ELE\",\"U02TTRYS7\",\"U02TU0KLR\",\"U02TVGRF6\",\"U02U5UULA\",\"U02U8RKR3\",\"U0302P1G3\",\"U031MU6L7\",\"U031YCFB8\",\"U0320HC20\",\"U033NHWDE\",\"U033PNZ44\",\"U033RMUJH\",\"U033T4SHE\",\"U033T5216\",\"U033TB01W\",\"U033TCE0W\",\"U033TSX9A\",\"U03404U57\",\"U03419JM6\",\"U034A3B71\",\"U034REYU6\",\"U03526226\",\"U037QLRHE\",\"U03F972EC\",\"U03JHB34V\",\"U03JKANBA\",\"U03LE2SNL\",\"U03NZ50P2\",\"U03SCFJSV\",\"U03SEN8RW\",\"U04EB26E0\"],\"topic\":{\"value\":\"\",\"creator\":\"\",\"last_set\":0},\"purpose\":{\"value\":\"This channel is for team-wide communication and announcements. All team members are in this channel.\",\"creator\":\"\",\"last_set\":0}},{\"id\":\"C03MQ96DQ\",\"name\":\"groundtruth\",\"is_channel\":true,\"created\":1424105575,\"creator\":\"U034A3B71\",\"is_archived\":false,\"is_general\":false,\"has_pins\":false,\"is_member\":true,\"members\":[\"U02T22LS0\",\"U02TVGRF6\",\"U02U8RKR3\",\"U031MU6L7\",\"U0320HC20\",\"U03404U57\",\"U03419JM6\",\"U034A3B71\",\"U034REYU6\",\"U037QLRHE\"],\"topic\":{\"value\":\"\",\"creator\":\"\",\"last_set\":0},\"purpose\":{\"value\":\"build a ground truth for training and validate the accuracy.\",\"creator\":\"U034A3B71\",\"last_set\":1424105793}},{\"id\":\"C03953AAF\",\"name\":\"hiring\",\"is_channel\":true,\"created\":1419967370,\"creator\":\"U02U5UULA\",\"is_archived\":false,\"is_general\":false,\"has_pins\":false,\"is_member\":false},{\"id\":\"C03019T4T\",\"name\":\"kt\",\"is_channel\":true,\"created\":1415886211,\"creator\":\"U02T22LS0\",\"is_archived\":false,\"is_general\":false,\"has_pins\":false,\"is_member\":false},{\"id\":\"C0340CU24\",\"name\":\"lab-meetings\",\"is_channel\":true,\"created\":1417621478,\"creator\":\"U02TC3ELE\",\"is_archived\":false,\"is_general\":false,\"is_starred\":true,\"has_pins\":false,\"is_member\":true,\"members\":[\"U02FH1DRC\",\"U02T22LS0\",\"U02TC3ELE\",\"U02TTRYS7\",\"U02TU0KLR\",\"U02TVGRF6\",\"U02U5UULA\",\"U02U8RKR3\",\"U0302P1G3\",\"U031MU6L7\",\"U031YCFB8\",\"U0320HC20\",\"U033NHWDE\",\"U033PNZ44\",\"U033TB01W\",\"U033TSX9A\",\"U03404U57\",\"U03419JM6\",\"U034A3B71\",\"U034REYU6\",\"U03526226\",\"U037QLRHE\",\"U03F972EC\",\"U03LE2SNL\"],\"topic\":{\"value\":\"\",\"creator\":\"\",\"last_set\":0},\"purpose\":{\"value\":\"Upcoming lab meetings, reschedulings, topics and everything else related\",\"creator\":\"U02TC3ELE\",\"last_set\":1417621478}},{\"id\":\"C035EUFSL\",\"name\":\"moving\",\"is_channel\":true,\"created\":1418181348,\"creator\":\"U02FH1DRC\",\"is_archived\":true,\"is_general\":false,\"has_pins\":false,\"is_member\":false},{\"id\":\"C03Q0RH5Z\",\"name\":\"music\",\"is_channel\":true,\"created\":1424735310,\"creator\":\"U03JHB34V\",\"is_archived\":false,\"is_general\":false,\"has_pins\":false,\"is_member\":false},{\"id\":\"C03AZ8MHM\",\"name\":\"music-exchange\",\"is_channel\":true,\"created\":1420835904,\"creator\":\"U033NHWDE\",\"is_archived\":false,\"is_general\":false,\"has_pins\":false,\"is_member\":false},{\"id\":\"C0453T75A\",\"name\":\"nyc\",\"is_channel\":true,\"created\":1427336681,\"creator\":\"U031YCFB8\",\"is_archived\":false,\"is_general\":false,\"has_pins\":false,\"is_member\":false},{\"id\":\"C03MNH5PC\",\"name\":\"piriform_cortex\",\"is_channel\":true,\"created\":1424095961,\"creator\":\"U034A3B71\",\"is_archived\":true,\"is_general\":false,\"has_pins\":false,\"is_member\":false},{\"id\":\"C036CHEAX\",\"name\":\"princeton\",\"is_channel\":true,\"created\":1418584733,\"creator\":\"U02FH1DRC\",\"is_archived\":false,\"is_general\":false,\"has_pins\":true,\"is_member\":true,\"members\":[\"U02FH1DRC\",\"U02T22LS0\",\"U02TTRYS7\",\"U02TU0KLR\",\"U02TVGRF6\",\"U02U5UULA\",\"U02U8RKR3\",\"U031MU6L7\",\"U0320HC20\",\"U033RMUJH\",\"U033T4SHE\",\"U033T5216\",\"U033TB01W\",\"U03404U57\",\"U03419JM6\",\"U034A3B71\",\"U034REYU6\",\"U037QLRHE\",\"U03LE2SNL\"],\"topic\":{\"value\":\"\",\"creator\":\"\",\"last_set\":0},\"purpose\":{\"value\":\"\",\"creator\":\"\",\"last_set\":0}},{\"id\":\"C02FH1DRL\",\"name\":\"random\",\"is_channel\":true,\"created\":1407542311,\"creator\":\"U02FH1DRC\",\"is_archived\":false,\"is_general\":false,\"has_pins\":false,\"is_member\":true,\"members\":[\"U02FH1DRC\",\"U02FH4TGY\",\"U02T22LS0\",\"U02TC3ELE\",\"U02TTRYS7\",\"U02TU0KLR\",\"U02TVGRF6\",\"U02U5UULA\",\"U02U8RKR3\",\"U0302P1G3\",\"U031MU6L7\",\"U031YCFB8\",\"U0320HC20\",\"U033NHWDE\",\"U033RMUJH\",\"U033T4SHE\",\"U033T5216\",\"U033TB01W\",\"U033TSX9A\",\"U03404U57\",\"U03419JM6\",\"U034A3B71\",\"U034REYU6\",\"U03526226\",\"U037QLRHE\",\"U03F972EC\",\"U03JHB34V\",\"U03JKANBA\",\"U03LE2SNL\",\"U03NZ50P2\",\"U03SCFJSV\",\"U03SEN8RW\",\"U04EB26E0\"],\"topic\":{\"value\":\"\",\"creator\":\"\",\"last_set\":0},\"purpose\":{\"value\":\"A place for non-work banter, links, articles of interest, humor or anything else which you\'d like concentrated in some place other than work-related channels.\",\"creator\":\"\",\"last_set\":0}},{\"id\":\"C03N859BC\",\"name\":\"retina\",\"is_channel\":true,\"created\":1424224473,\"creator\":\"U02TVGRF6\",\"is_archived\":false,\"is_general\":false,\"has_pins\":false,\"is_member\":false},{\"id\":\"C03K2CVG4\",\"name\":\"scythecomplete\",\"is_channel\":true,\"created\":1423280647,\"creator\":\"U02U5UULA\",\"is_archived\":false,\"is_general\":false,\"has_pins\":false,\"is_member\":false},{\"id\":\"C02U4GMPX\",\"name\":\"secret-santa\",\"is_channel\":true,\"created\":1415324812,\"creator\":\"U02FH1DRC\",\"is_archived\":true,\"is_general\":false,\"has_pins\":false,\"is_member\":false},{\"id\":\"C03PMV9MG\",\"name\":\"sound_design\",\"is_channel\":true,\"created\":1424624678,\"creator\":\"U03JHB34V\",\"is_archived\":false,\"is_general\":false,\"has_pins\":false,\"is_member\":false},{\"id\":\"C03CKSG47\",\"name\":\"stats\",\"is_channel\":true,\"created\":1421386724,\"creator\":\"U02FH1DRC\",\"is_archived\":false,\"is_general\":false,\"has_pins\":false,\"is_member\":true,\"members\":[\"U02FH1DRC\",\"U02T22LS0\",\"U02TC3ELE\",\"U02TU0KLR\",\"U02TVGRF6\",\"U02U5UULA\",\"U02U8RKR3\",\"U031MU6L7\",\"U031YCFB8\",\"U0320HC20\",\"U033NHWDE\",\"U033PNZ44\",\"U033RMUJH\",\"U033T5216\",\"U033TSX9A\",\"U034A3B71\",\"U034REYU6\"],\"topic\":{\"value\":\"\",\"creator\":\"\",\"last_set\":0},\"purpose\":{\"value\":\"for discussing stats. bot stats for motd are in channel #autostats\",\"creator\":\"U02FH1DRC\",\"last_set\":1421386725}},{\"id\":\"C036PUXKM\",\"name\":\"swaaag\",\"is_channel\":true,\"created\":1418701653,\"creator\":\"U02FH1DRC\",\"is_archived\":false,\"is_general\":false,\"has_pins\":false,\"is_member\":false},{\"id\":\"C03QH41AX\",\"name\":\"ted-ed\",\"is_channel\":true,\"created\":1424836892,\"creator\":\"U02TTRYS7\",\"is_archived\":true,\"is_general\":false,\"has_pins\":false,\"is_member\":false},{\"id\":\"C033T5AGA\",\"name\":\"tracers\",\"is_channel\":true,\"created\":1417537688,\"creator\":\"U02T22LS0\",\"is_archived\":false,\"is_general\":false,\"has_pins\":false,\"is_member\":true,\"members\":[\"U02FH1DRC\",\"U02TC3ELE\",\"U02U5UULA\",\"U02U8RKR3\",\"U031MU6L7\",\"U031YCFB8\",\"U0320HC20\",\"U033NHWDE\",\"U033PNZ44\",\"U033RMUJH\",\"U033T4SHE\",\"U033T5216\",\"U033TB01W\",\"U033TCE0W\",\"U033TSX9A\",\"U03404U57\",\"U03419JM6\",\"U034A3B71\",\"U037QLRHE\",\"U03JKANBA\"],\"topic\":{\"value\":\"\",\"creator\":\"\",\"last_set\":0},\"purpose\":{\"value\":\"All tracing related messages\",\"creator\":\"U02T22LS0\",\"last_set\":1417537689}},{\"id\":\"C03SS9DRN\",\"name\":\"translations\",\"is_channel\":true,\"created\":1425401498,\"creator\":\"U033NHWDE\",\"is_archived\":false,\"is_general\":false,\"has_pins\":false,\"is_member\":false},{\"id\":\"C03PAL6TY\",\"name\":\"watershed\",\"is_channel\":true,\"created\":1424461601,\"creator\":\"U03404U57\",\"is_archived\":false,\"is_general\":false,\"is_starred\":true,\"has_pins\":false,\"is_member\":true,\"members\":[\"U02T22LS0\",\"U02TVGRF6\",\"U02U8RKR3\",\"U031MU6L7\",\"U0320HC20\",\"U03404U57\",\"U03419JM6\",\"U034A3B71\",\"U034REYU6\"],\"topic\":{\"value\":\"\",\"creator\":\"\",\"last_set\":0},\"purpose\":{\"value\":\"\",\"creator\":\"\",\"last_set\":0}},{\"id\":\"C02TR5JRP\",\"name\":\"wd\",\"is_channel\":true,\"created\":1415207579,\"creator\":\"U02FH1DRC\",\"is_archived\":false,\"is_general\":false,\"has_pins\":false,\"is_member\":false},{\"id\":\"C04EYRH5T\",\"name\":\"wizardofneuropia\",\"is_channel\":true,\"created\":1429286150,\"creator\":\"U02FH1DRC\",\"is_archived\":false,\"is_general\":false,\"has_pins\":false,\"is_member\":false},{\"id\":\"C034NFGUU\",\"name\":\"znn\",\"is_channel\":true,\"created\":1417820785,\"creator\":\"U034A3B71\",\"is_archived\":false,\"is_general\":false,\"is_starred\":true,\"has_pins\":false,\"is_member\":true,\"members\":[\"U02FH1DRC\",\"U02T22LS0\",\"U02TC3ELE\",\"U02TVGRF6\",\"U02U5UULA\",\"U02U8RKR3\",\"U031MU6L7\",\"U0320HC20\",\"U03404U57\",\"U03419JM6\",\"U034A3B71\",\"U034REYU6\",\"U03LE2SNL\"],\"topic\":{\"value\":\"\",\"creator\":\"\",\"last_set\":0},\"purpose\":{\"value\":\"test and applying ZNN to EM data.\",\"creator\":\"U034A3B71\",\"last_set\":1417873427}},{\"id\":\"C03VDMXGZ\",\"name\":\"znn-paper\",\"is_channel\":true,\"created\":1426037748,\"creator\":\"U03404U57\",\"is_archived\":false,\"is_general\":false,\"is_starred\":true,\"has_pins\":false,\"is_member\":true,\"members\":[\"U02TVGRF6\",\"U03404U57\",\"U034A3B71\",\"U034REYU6\"],\"topic\":{\"value\":\"\",\"creator\":\"\",\"last_set\":0},\"purpose\":{\"value\":\"Schedule meetings, discuss stuff..\",\"creator\":\"U03404U57\",\"last_set\":1426037748}}],\"groups\":[],\"ims\":[{\"id\":\"D034A3B87\",\"is_im\":true,\"user\":\"USLACKBOT\",\"created\":1417723049,\"is_user_deleted\":false},{\"id\":\"D034A3B8H\",\"is_im\":true,\"user\":\"U02FH1DRC\",\"created\":1417723049,\"is_user_deleted\":false},{\"id\":\"D034A3BAD\",\"is_im\":true,\"user\":\"U02FH4TGY\",\"created\":1417723049,\"is_user_deleted\":true},{\"id\":\"D034A3H3F\",\"is_im\":true,\"user\":\"U02T22LS0\",\"created\":1417723108,\"is_starred\":true,\"is_user_deleted\":false},{\"id\":\"D034A3B99\",\"is_im\":true,\"user\":\"U02TC3ELE\",\"created\":1417723049,\"is_user_deleted\":false},{\"id\":\"D038Z0WGS\",\"is_im\":true,\"user\":\"U02TTRYS7\",\"created\":1419871627,\"is_user_deleted\":false},{\"id\":\"D0358PB53\",\"is_im\":true,\"user\":\"U02TU0KLR\",\"created\":1418144436,\"is_user_deleted\":false},{\"id\":\"D034A3B91\",\"is_im\":true,\"user\":\"U02TVGRF6\",\"created\":1417723049,\"is_starred\":true,\"is_user_deleted\":false},{\"id\":\"D0388DZ0Z\",\"is_im\":true,\"user\":\"U02U8RKR3\",\"created\":1419352765,\"is_starred\":true,\"is_user_deleted\":false},{\"id\":\"D034A3BA3\",\"is_im\":true,\"user\":\"U031MU6L7\",\"created\":1417723049,\"is_starred\":true,\"is_user_deleted\":false},{\"id\":\"D034A3B9X\",\"is_im\":true,\"user\":\"U0320HC20\",\"created\":1417723049,\"is_user_deleted\":false},{\"id\":\"D034A3B9R\",\"is_im\":true,\"user\":\"U033NHWDE\",\"created\":1417723049,\"is_user_deleted\":false},{\"id\":\"D034A3B9H\",\"is_im\":true,\"user\":\"U033RMUJH\",\"created\":1417723049,\"is_user_deleted\":false},{\"id\":\"D034A3B8R\",\"is_im\":true,\"user\":\"U033T4SHE\",\"created\":1417723049,\"is_user_deleted\":false},{\"id\":\"D034A3B95\",\"is_im\":true,\"user\":\"U03404U57\",\"created\":1417723049,\"is_starred\":true,\"is_user_deleted\":false},{\"id\":\"D0381SN4P\",\"is_im\":true,\"user\":\"U03419JM6\",\"created\":1419272902,\"is_starred\":true,\"is_user_deleted\":false},{\"id\":\"D0353RQHC\",\"is_im\":true,\"user\":\"U034REYU6\",\"created\":1418080944,\"is_starred\":true,\"is_user_deleted\":false},{\"id\":\"D03526234\",\"is_im\":true,\"user\":\"U03526226\",\"created\":1418068576,\"is_user_deleted\":false},{\"id\":\"D037QLRJA\",\"is_im\":true,\"user\":\"U037QLRHE\",\"created\":1419026272,\"is_starred\":true,\"is_user_deleted\":false},{\"id\":\"D03JHB36X\",\"is_im\":true,\"user\":\"U03JHB34V\",\"created\":1423161328,\"is_user_deleted\":false},{\"id\":\"D03LE2SPY\",\"is_im\":true,\"user\":\"U03LE2SNL\",\"created\":1423693070,\"is_user_deleted\":false},{\"id\":\"D03NZ50R4\",\"is_im\":true,\"user\":\"U03NZ50P2\",\"created\":1424384898,\"is_user_deleted\":false}],\"users\":[{\"id\":\"U0302P1G3\",\"name\":\"albina\",\"deleted\":false,\"status\":null,\"color\":\"2b6836\",\"real_name\":\"\",\"tz\":\"America\\/Indiana\\/Indianapolis\",\"tz_label\":\"Eastern Daylight Time\",\"tz_offset\":-14400,\"profile\":{\"real_name\":\"\",\"real_name_normalized\":\"\",\"email\":\"biancad@princeton.edu\",\"image_24\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/60eb4f7c08d114b892579d4323dcc2fb.jpg?s=24&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0007-24.png\",\"image_32\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/60eb4f7c08d114b892579d4323dcc2fb.jpg?s=32&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0007-32.png\",\"image_48\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/60eb4f7c08d114b892579d4323dcc2fb.jpg?s=48&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0007-48.png\",\"image_72\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/60eb4f7c08d114b892579d4323dcc2fb.jpg?s=72&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0007-72.png\",\"image_192\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/60eb4f7c08d114b892579d4323dcc2fb.jpg?s=192&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F272a%2Fimg%2Favatars%2Fava_0007.png\"},\"is_admin\":false,\"is_owner\":false,\"is_primary_owner\":false,\"is_restricted\":false,\"is_ultra_restricted\":false,\"is_bot\":false},{\"id\":\"U02FH1DRC\",\"name\":\"amy\",\"deleted\":false,\"status\":null,\"color\":\"9f69e7\",\"real_name\":\"Amy Robinson\",\"tz\":\"America\\/Indiana\\/Indianapolis\",\"tz_label\":\"Eastern Daylight Time\",\"tz_offset\":-14400,\"profile\":{\"first_name\":\"Amy\",\"last_name\":\"Robinson\",\"image_24\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2014-11-06\\/2958240132_dc7b2f3c4179d652cb7b_24.jpg\",\"image_32\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2014-11-06\\/2958240132_dc7b2f3c4179d652cb7b_32.jpg\",\"image_48\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2014-11-06\\/2958240132_dc7b2f3c4179d652cb7b_48.jpg\",\"image_72\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2014-11-06\\/2958240132_dc7b2f3c4179d652cb7b_72.jpg\",\"image_192\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2014-11-06\\/2958240132_dc7b2f3c4179d652cb7b_192.jpg\",\"image_original\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2014-11-06\\/2958240132_dc7b2f3c4179d652cb7b_original.jpg\",\"skype\":\"<search>\",\"phone\":\"<search> jurassic park\",\"title\":\"want to go to space\",\"real_name\":\"Amy Robinson\",\"real_name_normalized\":\"Amy Robinson\",\"email\":\"amy@eyewire.org\"},\"is_admin\":true,\"is_owner\":true,\"is_primary_owner\":true,\"is_restricted\":false,\"is_ultra_restricted\":false,\"is_bot\":false},{\"id\":\"U03419JM6\",\"name\":\"ashwin\",\"deleted\":false,\"status\":null,\"color\":\"c386df\",\"real_name\":\"Ashwin Vishwanathan\",\"tz\":\"America\\/Indiana\\/Indianapolis\",\"tz_label\":\"Eastern Daylight Time\",\"tz_offset\":-14400,\"profile\":{\"first_name\":\"Ashwin\",\"last_name\":\"Vishwanathan\",\"real_name\":\"Ashwin Vishwanathan\",\"real_name_normalized\":\"Ashwin Vishwanathan\",\"email\":\"vishwanathan.ashwin@gmail.com\",\"image_24\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/3448f30013686d41c611220eb8d5f7c9.jpg?s=24&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0018-24.png\",\"image_32\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/3448f30013686d41c611220eb8d5f7c9.jpg?s=32&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0018-32.png\",\"image_48\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/3448f30013686d41c611220eb8d5f7c9.jpg?s=48&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F272a%2Fimg%2Favatars%2Fava_0018-48.png\",\"image_72\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/3448f30013686d41c611220eb8d5f7c9.jpg?s=72&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0018-72.png\",\"image_192\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/3448f30013686d41c611220eb8d5f7c9.jpg?s=192&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0018.png\"},\"is_admin\":false,\"is_owner\":false,\"is_primary_owner\":false,\"is_restricted\":false,\"is_ultra_restricted\":false,\"is_bot\":false},{\"id\":\"U033T4SHE\",\"name\":\"bun\",\"deleted\":false,\"status\":null,\"color\":\"5a4592\",\"real_name\":\"Ben Silverman\",\"tz\":\"America\\/Indiana\\/Indianapolis\",\"tz_label\":\"Eastern Daylight Time\",\"tz_offset\":-14400,\"profile\":{\"first_name\":\"Ben\",\"last_name\":\"Silverman\",\"image_24\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2015-04-07\\/4354863155_e6191c7f66d067e01e8c_24.jpg\",\"image_32\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2015-04-07\\/4354863155_e6191c7f66d067e01e8c_32.jpg\",\"image_48\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2015-04-07\\/4354863155_e6191c7f66d067e01e8c_48.jpg\",\"image_72\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2015-04-07\\/4354863155_e6191c7f66d067e01e8c_72.jpg\",\"image_192\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2015-04-07\\/4354863155_e6191c7f66d067e01e8c_192.jpg\",\"image_original\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2015-04-07\\/4354863155_e6191c7f66d067e01e8c_original.jpg\",\"real_name\":\"Ben Silverman\",\"real_name_normalized\":\"Ben Silverman\",\"email\":\"benjamindsilverman@gmail.com\"},\"is_admin\":false,\"is_owner\":false,\"is_primary_owner\":false,\"is_restricted\":false,\"is_ultra_restricted\":false,\"is_bot\":false},{\"id\":\"U033NHWDE\",\"name\":\"celia\",\"deleted\":false,\"status\":null,\"color\":\"9b3b45\",\"real_name\":\"Celia D\",\"tz\":\"America\\/Indiana\\/Indianapolis\",\"tz_label\":\"Eastern Daylight Time\",\"tz_offset\":-14400,\"profile\":{\"first_name\":\"Celia\",\"last_name\":\"D\",\"title\":\"\",\"skype\":\"\",\"phone\":\"\",\"real_name\":\"Celia D\",\"real_name_normalized\":\"Celia D\",\"email\":\"celia@eyewire.org\",\"image_24\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/af421031d6e471e52a49b08b9b77ef09.jpg?s=24&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0011-24.png\",\"image_32\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/af421031d6e471e52a49b08b9b77ef09.jpg?s=32&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0011-32.png\",\"image_48\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/af421031d6e471e52a49b08b9b77ef09.jpg?s=48&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0011-48.png\",\"image_72\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/af421031d6e471e52a49b08b9b77ef09.jpg?s=72&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0011-72.png\",\"image_192\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/af421031d6e471e52a49b08b9b77ef09.jpg?s=192&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0011.png\"},\"is_admin\":true,\"is_owner\":false,\"is_primary_owner\":false,\"is_restricted\":false,\"is_ultra_restricted\":false,\"is_bot\":false},{\"id\":\"U031YCFB8\",\"name\":\"chris\",\"deleted\":false,\"status\":null,\"color\":\"df3dc0\",\"real_name\":\"Chris Jordan\",\"tz\":\"America\\/Indiana\\/Indianapolis\",\"tz_label\":\"Eastern Daylight Time\",\"tz_offset\":-14400,\"profile\":{\"first_name\":\"Chris\",\"last_name\":\"Jordan\",\"real_name\":\"Chris Jordan\",\"real_name_normalized\":\"Chris Jordan\",\"email\":\"chris@eyewire.org\",\"image_24\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/8220c368e65ced136160ec1d84e8bdea.jpg?s=24&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0022-24.png\",\"image_32\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/8220c368e65ced136160ec1d84e8bdea.jpg?s=32&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0022-32.png\",\"image_48\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/8220c368e65ced136160ec1d84e8bdea.jpg?s=48&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0022-48.png\",\"image_72\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/8220c368e65ced136160ec1d84e8bdea.jpg?s=72&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0022-72.png\",\"image_192\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/8220c368e65ced136160ec1d84e8bdea.jpg?s=192&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0022.png\"},\"is_admin\":false,\"is_owner\":false,\"is_primary_owner\":false,\"is_restricted\":false,\"is_ultra_restricted\":false,\"is_bot\":false},{\"id\":\"U03SEN8RW\",\"name\":\"curtislb\",\"deleted\":false,\"status\":null,\"color\":\"de5f24\",\"real_name\":\"Curtis Belmonte\",\"tz\":\"America\\/Indiana\\/Indianapolis\",\"tz_label\":\"Eastern Daylight Time\",\"tz_offset\":-14400,\"profile\":{\"first_name\":\"Curtis\",\"last_name\":\"Belmonte\",\"image_24\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2015-03-02\\/3896755401_e824af5264075086b398_24.jpg\",\"image_32\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2015-03-02\\/3896755401_e824af5264075086b398_32.jpg\",\"image_48\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2015-03-02\\/3896755401_e824af5264075086b398_48.jpg\",\"image_72\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2015-03-02\\/3896755401_e824af5264075086b398_72.jpg\",\"image_192\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2015-03-02\\/3896755401_e824af5264075086b398_192.jpg\",\"image_original\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2015-03-02\\/3896755401_e824af5264075086b398_original.jpg\",\"real_name\":\"Curtis Belmonte\",\"real_name_normalized\":\"Curtis Belmonte\",\"email\":\"curtislb@princeton.edu\"},\"is_admin\":false,\"is_owner\":false,\"is_primary_owner\":false,\"is_restricted\":false,\"is_ultra_restricted\":false,\"is_bot\":false},{\"id\":\"U037QLRHE\",\"name\":\"daanvisser\",\"deleted\":false,\"status\":null,\"color\":\"50a0cf\",\"real_name\":\"\",\"tz\":\"America\\/Indiana\\/Indianapolis\",\"tz_label\":\"Eastern Daylight Time\",\"tz_offset\":-14400,\"profile\":{\"image_24\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2015-04-03\\/4318661065_5c8517064bc7c2201f58_24.jpg\",\"image_32\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2015-04-03\\/4318661065_5c8517064bc7c2201f58_32.jpg\",\"image_48\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2015-04-03\\/4318661065_5c8517064bc7c2201f58_48.jpg\",\"image_72\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2015-04-03\\/4318661065_5c8517064bc7c2201f58_72.jpg\",\"image_192\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2015-04-03\\/4318661065_5c8517064bc7c2201f58_192.jpg\",\"image_original\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2015-04-03\\/4318661065_5c8517064bc7c2201f58_original.jpg\",\"real_name\":\"\",\"real_name_normalized\":\"\",\"email\":\"jvisser@princeton.edu\"},\"is_admin\":false,\"is_owner\":false,\"is_primary_owner\":false,\"is_restricted\":false,\"is_ultra_restricted\":false,\"is_bot\":false},{\"id\":\"U033TCE0W\",\"name\":\"devonjones\",\"deleted\":false,\"status\":null,\"color\":\"9e3997\",\"real_name\":\"Devon Jones\",\"tz\":\"America\\/Indiana\\/Indianapolis\",\"tz_label\":\"Eastern Daylight Time\",\"tz_offset\":-14400,\"profile\":{\"first_name\":\"Devon\",\"last_name\":\"Jones\",\"title\":\"Game Master\",\"skype\":\"\",\"phone\":\"(603) 721-1819\",\"image_24\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2015-04-08\\/4377064469_18f3c3d3b3db564f9e4d_24.jpg\",\"image_32\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2015-04-08\\/4377064469_18f3c3d3b3db564f9e4d_32.jpg\",\"image_48\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2015-04-08\\/4377064469_18f3c3d3b3db564f9e4d_48.jpg\",\"image_72\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2015-04-08\\/4377064469_18f3c3d3b3db564f9e4d_72.jpg\",\"image_192\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2015-04-08\\/4377064469_18f3c3d3b3db564f9e4d_192.jpg\",\"image_original\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2015-04-08\\/4377064469_18f3c3d3b3db564f9e4d_original.jpg\",\"real_name\":\"Devon Jones\",\"real_name_normalized\":\"Devon Jones\",\"email\":\"linguist.devon@gmail.com\"},\"is_admin\":false,\"is_owner\":false,\"is_primary_owner\":false,\"is_restricted\":false,\"is_ultra_restricted\":false,\"is_bot\":false},{\"id\":\"U02TVGRF6\",\"name\":\"hsseung\",\"deleted\":false,\"status\":null,\"color\":\"e0a729\",\"real_name\":\"Sebastian Seung\",\"tz\":\"America\\/Indiana\\/Indianapolis\",\"tz_label\":\"Eastern Daylight Time\",\"tz_offset\":-14400,\"profile\":{\"first_name\":\"Sebastian\",\"last_name\":\"Seung\",\"real_name\":\"Sebastian Seung\",\"real_name_normalized\":\"Sebastian Seung\",\"email\":\"sseung@princeton.edu\",\"image_24\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/2b3bcad0866fb2506d31a36191bfbbff.jpg?s=24&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0005-24.png\",\"image_32\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/2b3bcad0866fb2506d31a36191bfbbff.jpg?s=32&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0005-32.png\",\"image_48\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/2b3bcad0866fb2506d31a36191bfbbff.jpg?s=48&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0005-48.png\",\"image_72\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/2b3bcad0866fb2506d31a36191bfbbff.jpg?s=72&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0005-72.png\",\"image_192\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/2b3bcad0866fb2506d31a36191bfbbff.jpg?s=192&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0005.png\"},\"is_admin\":false,\"is_owner\":false,\"is_primary_owner\":false,\"is_restricted\":false,\"is_ultra_restricted\":false,\"is_bot\":false},{\"id\":\"U034A3B71\",\"name\":\"jingpeng\",\"deleted\":false,\"status\":null,\"color\":\"a63024\",\"real_name\":\"Jingpeng Wu\",\"tz\":\"America\\/Indiana\\/Indianapolis\",\"tz_label\":\"Eastern Daylight Time\",\"tz_offset\":-14400,\"profile\":{\"first_name\":\"Jingpeng\",\"last_name\":\"Wu\",\"skype\":\"s09olbj\",\"title\":\"Postdoc\",\"phone\":\"(609)-216-4179\",\"real_name\":\"Jingpeng Wu\",\"real_name_normalized\":\"Jingpeng Wu\",\"email\":\"jingpeng@princeton.edu\",\"image_24\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/6e3c17d7fd502ce0426b632be329381b.jpg?s=24&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F272a%2Fimg%2Favatars%2Fava_0001-24.png\",\"image_32\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/6e3c17d7fd502ce0426b632be329381b.jpg?s=32&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0001-32.png\",\"image_48\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/6e3c17d7fd502ce0426b632be329381b.jpg?s=48&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0001-48.png\",\"image_72\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/6e3c17d7fd502ce0426b632be329381b.jpg?s=72&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0001-72.png\",\"image_192\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/6e3c17d7fd502ce0426b632be329381b.jpg?s=192&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0001.png\"},\"is_admin\":false,\"is_owner\":false,\"is_primary_owner\":false,\"is_restricted\":false,\"is_ultra_restricted\":false,\"is_bot\":false},{\"id\":\"U031MU6L7\",\"name\":\"jinseop\",\"deleted\":false,\"status\":null,\"color\":\"99a949\",\"real_name\":\"Jinseop Kim\",\"tz\":\"America\\/Indiana\\/Indianapolis\",\"tz_label\":\"Eastern Daylight Time\",\"tz_offset\":-14400,\"profile\":{\"first_name\":\"Jinseop\",\"last_name\":\"Kim\",\"real_name\":\"Jinseop Kim\",\"real_name_normalized\":\"Jinseop Kim\",\"email\":\"jinseopk@princeton.edu\",\"image_24\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/a3ab312403bf1ff78bfd676237bee6fc.jpg?s=24&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0025-24.png\",\"image_32\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/a3ab312403bf1ff78bfd676237bee6fc.jpg?s=32&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0025-32.png\",\"image_48\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/a3ab312403bf1ff78bfd676237bee6fc.jpg?s=48&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0025-48.png\",\"image_72\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/a3ab312403bf1ff78bfd676237bee6fc.jpg?s=72&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0025-72.png\",\"image_192\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/a3ab312403bf1ff78bfd676237bee6fc.jpg?s=192&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0025.png\"},\"is_admin\":false,\"is_owner\":false,\"is_primary_owner\":false,\"is_restricted\":false,\"is_ultra_restricted\":false,\"is_bot\":false},{\"id\":\"U03JHB34V\",\"name\":\"john\",\"deleted\":false,\"status\":null,\"color\":\"43761b\",\"real_name\":\"John Smith\",\"tz\":\"America\\/Indiana\\/Indianapolis\",\"tz_label\":\"Eastern Daylight Time\",\"tz_offset\":-14400,\"profile\":{\"first_name\":\"John\",\"last_name\":\"Smith\",\"real_name\":\"John Smith\",\"real_name_normalized\":\"John Smith\",\"email\":\"john@eyewire.org\",\"image_24\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/75e748154711b5463b652a030ec4c4c4.jpg?s=24&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0002-24.png\",\"image_32\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/75e748154711b5463b652a030ec4c4c4.jpg?s=32&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0002-32.png\",\"image_48\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/75e748154711b5463b652a030ec4c4c4.jpg?s=48&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F272a%2Fimg%2Favatars%2Fava_0002-48.png\",\"image_72\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/75e748154711b5463b652a030ec4c4c4.jpg?s=72&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0002-72.png\",\"image_192\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/75e748154711b5463b652a030ec4c4c4.jpg?s=192&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0002.png\"},\"is_admin\":false,\"is_owner\":false,\"is_primary_owner\":false,\"is_restricted\":false,\"is_ultra_restricted\":false,\"is_bot\":false},{\"id\":\"U03526226\",\"name\":\"jonathanzung\",\"deleted\":false,\"status\":null,\"color\":\"ea2977\",\"real_name\":\"Jonathan Zung\",\"tz\":\"America\\/Indiana\\/Indianapolis\",\"tz_label\":\"Eastern Daylight Time\",\"tz_offset\":-14400,\"profile\":{\"first_name\":\"Jonathan\",\"last_name\":\"Zung\",\"title\":\"Slacker\",\"real_name\":\"Jonathan Zung\",\"real_name_normalized\":\"Jonathan Zung\",\"email\":\"jzung@princeton.edu\",\"image_24\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/1145a72b8bc7928366fe2a6b192ed15f.jpg?s=24&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0010-24.png\",\"image_32\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/1145a72b8bc7928366fe2a6b192ed15f.jpg?s=32&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0010-32.png\",\"image_48\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/1145a72b8bc7928366fe2a6b192ed15f.jpg?s=48&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0010-48.png\",\"image_72\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/1145a72b8bc7928366fe2a6b192ed15f.jpg?s=72&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0010-72.png\",\"image_192\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/1145a72b8bc7928366fe2a6b192ed15f.jpg?s=192&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0010.png\"},\"is_admin\":false,\"is_owner\":false,\"is_primary_owner\":false,\"is_restricted\":false,\"is_ultra_restricted\":false,\"is_bot\":false},{\"id\":\"U03NZ50P2\",\"name\":\"juliansamal\",\"deleted\":false,\"status\":null,\"color\":\"8f4a2b\",\"real_name\":\"\",\"tz\":\"America\\/Indiana\\/Indianapolis\",\"tz_label\":\"Eastern Daylight Time\",\"tz_offset\":-14400,\"profile\":{\"real_name\":\"\",\"real_name_normalized\":\"\",\"email\":\"jsamal@berklee.edu\",\"image_24\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/8f79948cc56aae3968df5856d2770e8a.jpg?s=24&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0009-24.png\",\"image_32\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/8f79948cc56aae3968df5856d2770e8a.jpg?s=32&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0009-32.png\",\"image_48\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/8f79948cc56aae3968df5856d2770e8a.jpg?s=48&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0009-48.png\",\"image_72\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/8f79948cc56aae3968df5856d2770e8a.jpg?s=72&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0009-72.png\",\"image_192\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/8f79948cc56aae3968df5856d2770e8a.jpg?s=192&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0009.png\"},\"is_admin\":false,\"is_owner\":false,\"is_primary_owner\":false,\"is_restricted\":false,\"is_ultra_restricted\":false,\"is_bot\":false},{\"id\":\"U034REYU6\",\"name\":\"kisuklee\",\"deleted\":false,\"status\":null,\"color\":\"5870dd\",\"real_name\":\"Kisuk Lee\",\"tz\":\"America\\/Indiana\\/Indianapolis\",\"tz_label\":\"Eastern Daylight Time\",\"tz_offset\":-14400,\"profile\":{\"first_name\":\"Kisuk\",\"last_name\":\"Lee\",\"real_name\":\"Kisuk Lee\",\"real_name_normalized\":\"Kisuk Lee\",\"email\":\"kisuklee@mit.edu\",\"image_24\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/7b500c9c336cc8b680f32f9d9dc39a17.jpg?s=24&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0008-24.png\",\"image_32\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/7b500c9c336cc8b680f32f9d9dc39a17.jpg?s=32&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0008-32.png\",\"image_48\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/7b500c9c336cc8b680f32f9d9dc39a17.jpg?s=48&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0008-48.png\",\"image_72\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/7b500c9c336cc8b680f32f9d9dc39a17.jpg?s=72&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0008-72.png\",\"image_192\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/7b500c9c336cc8b680f32f9d9dc39a17.jpg?s=192&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0008.png\"},\"is_admin\":false,\"is_owner\":false,\"is_primary_owner\":false,\"is_restricted\":false,\"is_ultra_restricted\":false,\"is_bot\":false},{\"id\":\"U03F972EC\",\"name\":\"matt\",\"deleted\":false,\"status\":null,\"color\":\"d55aef\",\"real_name\":\"\",\"tz\":\"America\\/Indiana\\/Indianapolis\",\"tz_label\":\"Eastern Daylight Time\",\"tz_offset\":-14400,\"profile\":{\"real_name\":\"\",\"real_name_normalized\":\"\",\"email\":\"greenem@mit.edu\",\"image_24\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/dabb4a57d91b1c0660f78cefc0feee36.jpg?s=24&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0026-24.png\",\"image_32\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/dabb4a57d91b1c0660f78cefc0feee36.jpg?s=32&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0026-32.png\",\"image_48\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/dabb4a57d91b1c0660f78cefc0feee36.jpg?s=48&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F272a%2Fimg%2Favatars%2Fava_0026-48.png\",\"image_72\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/dabb4a57d91b1c0660f78cefc0feee36.jpg?s=72&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0026-72.png\",\"image_192\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/dabb4a57d91b1c0660f78cefc0feee36.jpg?s=192&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F272a%2Fimg%2Favatars%2Fava_0026.png\"},\"is_admin\":false,\"is_owner\":false,\"is_primary_owner\":false,\"is_restricted\":false,\"is_ultra_restricted\":false,\"is_bot\":false},{\"id\":\"U033TB01W\",\"name\":\"merlmoor\",\"deleted\":false,\"status\":null,\"color\":\"235e5b\",\"real_name\":\"Merlin Moore\",\"tz\":\"America\\/Indiana\\/Indianapolis\",\"tz_label\":\"Eastern Daylight Time\",\"tz_offset\":-14400,\"profile\":{\"first_name\":\"Merlin\",\"last_name\":\"Moore\",\"real_name\":\"Merlin Moore\",\"real_name_normalized\":\"Merlin Moore\",\"email\":\"merlmoor@scarletmail.rutgers.edu\",\"image_24\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/972e411ca12fa1f732ed61773b3c6ada.jpg?s=24&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0006-24.png\",\"image_32\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/972e411ca12fa1f732ed61773b3c6ada.jpg?s=32&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0006-32.png\",\"image_48\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/972e411ca12fa1f732ed61773b3c6ada.jpg?s=48&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0006-48.png\",\"image_72\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/972e411ca12fa1f732ed61773b3c6ada.jpg?s=72&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0006-72.png\",\"image_192\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/972e411ca12fa1f732ed61773b3c6ada.jpg?s=192&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0006.png\"},\"is_admin\":false,\"is_owner\":false,\"is_primary_owner\":false,\"is_restricted\":false,\"is_ultra_restricted\":false,\"is_bot\":false},{\"id\":\"U03SCFJSV\",\"name\":\"mina\",\"deleted\":false,\"status\":null,\"color\":\"902d59\",\"real_name\":\"Mina\",\"tz\":\"America\\/Indiana\\/Indianapolis\",\"tz_label\":\"Eastern Daylight Time\",\"tz_offset\":-14400,\"profile\":{\"first_name\":\"Mina\",\"real_name\":\"Mina\",\"real_name_normalized\":\"Mina\",\"email\":\"mina@eyewire.org\",\"image_24\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/6f2ad8e40167a6fd7502f7e9c28f26fd.jpg?s=24&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0010-24.png\",\"image_32\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/6f2ad8e40167a6fd7502f7e9c28f26fd.jpg?s=32&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0010-32.png\",\"image_48\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/6f2ad8e40167a6fd7502f7e9c28f26fd.jpg?s=48&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0010-48.png\",\"image_72\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/6f2ad8e40167a6fd7502f7e9c28f26fd.jpg?s=72&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0010-72.png\",\"image_192\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/6f2ad8e40167a6fd7502f7e9c28f26fd.jpg?s=192&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0010.png\"},\"is_admin\":false,\"is_owner\":false,\"is_primary_owner\":false,\"is_restricted\":false,\"is_ultra_restricted\":false,\"is_bot\":false},{\"id\":\"U02TU0KLR\",\"name\":\"miopio\",\"deleted\":false,\"status\":null,\"color\":\"e96699\",\"real_name\":\"Mio\",\"tz\":\"America\\/Indiana\\/Indianapolis\",\"tz_label\":\"Eastern Daylight Time\",\"tz_offset\":-14400,\"profile\":{\"image_24\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2014-12-03\\/3136878423_919b64fd4a897b536898_24.jpg\",\"image_32\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2014-12-03\\/3136878423_919b64fd4a897b536898_32.jpg\",\"image_48\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2014-12-03\\/3136878423_919b64fd4a897b536898_48.jpg\",\"image_72\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2014-12-03\\/3136878423_919b64fd4a897b536898_72.jpg\",\"image_192\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2014-12-03\\/3136878423_919b64fd4a897b536898_192.jpg\",\"image_original\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2014-12-03\\/3136878423_919b64fd4a897b536898_original.jpg\",\"first_name\":\"Mio\",\"last_name\":\"\",\"title\":\"\",\"skype\":\"\",\"phone\":\"\",\"real_name\":\"Mio\",\"real_name_normalized\":\"Mio\",\"email\":\"makasako@princeton.edu\"},\"is_admin\":false,\"is_owner\":false,\"is_primary_owner\":false,\"is_restricted\":false,\"is_ultra_restricted\":false,\"is_bot\":false},{\"id\":\"U03LE2SNL\",\"name\":\"nicholas_turner\",\"deleted\":false,\"status\":null,\"color\":\"e06b56\",\"real_name\":\"Nicholas Turner\",\"tz\":\"America\\/Indiana\\/Indianapolis\",\"tz_label\":\"Eastern Daylight Time\",\"tz_offset\":-14400,\"profile\":{\"first_name\":\"Nicholas\",\"last_name\":\"Turner\",\"image_24\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2015-02-11\\/3692853511_7e963f58251f363f3ac9_24.jpg\",\"image_32\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2015-02-11\\/3692853511_7e963f58251f363f3ac9_32.jpg\",\"image_48\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2015-02-11\\/3692853511_7e963f58251f363f3ac9_48.jpg\",\"image_72\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2015-02-11\\/3692853511_7e963f58251f363f3ac9_72.jpg\",\"image_192\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2015-02-11\\/3692853511_7e963f58251f363f3ac9_192.jpg\",\"image_original\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2015-02-11\\/3692853511_7e963f58251f363f3ac9_original.jpg\",\"real_name\":\"Nicholas Turner\",\"real_name_normalized\":\"Nicholas Turner\",\"email\":\"nturner@cs.princeton.edu\"},\"is_admin\":false,\"is_owner\":false,\"is_primary_owner\":false,\"is_restricted\":false,\"is_ultra_restricted\":false,\"is_bot\":false},{\"id\":\"U03JKANBA\",\"name\":\"nina\",\"deleted\":false,\"status\":null,\"color\":\"d1707d\",\"real_name\":\"\",\"tz\":\"America\\/Indiana\\/Indianapolis\",\"tz_label\":\"Eastern Daylight Time\",\"tz_offset\":-14400,\"profile\":{\"real_name\":\"\",\"real_name_normalized\":\"\",\"email\":\"nina@eyewire.org\",\"image_24\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/a005510d91cb3bdb12a2363c76e5fc74.jpg?s=24&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0017-24.png\",\"image_32\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/a005510d91cb3bdb12a2363c76e5fc74.jpg?s=32&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0017-32.png\",\"image_48\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/a005510d91cb3bdb12a2363c76e5fc74.jpg?s=48&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0017-48.png\",\"image_72\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/a005510d91cb3bdb12a2363c76e5fc74.jpg?s=72&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0017-72.png\",\"image_192\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/a005510d91cb3bdb12a2363c76e5fc74.jpg?s=192&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0017.png\"},\"is_admin\":false,\"is_owner\":false,\"is_primary_owner\":false,\"is_restricted\":false,\"is_ultra_restricted\":false,\"is_bot\":false},{\"id\":\"U02TC3ELE\",\"name\":\"nkem\",\"deleted\":false,\"status\":null,\"color\":\"3c989f\",\"real_name\":\"Nico Kemnitz\",\"tz\":\"Europe\\/Amsterdam\",\"tz_label\":\"Central European Summer Time\",\"tz_offset\":7200,\"profile\":{\"first_name\":\"Nico\",\"last_name\":\"Kemnitz\",\"image_24\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2014-11-10\\/2976301897_b2f8627f067c21993d50_24.jpg\",\"image_32\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2014-11-10\\/2976301897_b2f8627f067c21993d50_32.jpg\",\"image_48\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2014-11-10\\/2976301897_b2f8627f067c21993d50_48.jpg\",\"image_72\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2014-11-10\\/2976301897_b2f8627f067c21993d50_72.jpg\",\"image_192\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2014-11-10\\/2976301897_b2f8627f067c21993d50_192.jpg\",\"image_original\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2014-11-10\\/2976301897_b2f8627f067c21993d50_original.jpg\",\"skype\":\"live:nkem_13\",\"title\":\"Slackbot! Wie geht\'s?\",\"phone\":\"\",\"real_name\":\"Nico Kemnitz\",\"real_name_normalized\":\"Nico Kemnitz\",\"email\":\"nico@eyewire.org\"},\"is_admin\":false,\"is_owner\":false,\"is_primary_owner\":false,\"is_restricted\":false,\"is_ultra_restricted\":false,\"is_bot\":false},{\"id\":\"U033T5216\",\"name\":\"rocksteady\",\"deleted\":false,\"status\":null,\"color\":\"db3150\",\"real_name\":\"Mike Weiss\",\"tz\":\"America\\/Indiana\\/Indianapolis\",\"tz_label\":\"Eastern Daylight Time\",\"tz_offset\":-14400,\"profile\":{\"first_name\":\"Mike\",\"last_name\":\"Weiss\",\"image_24\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2015-03-12\\/4026132781_fd82554431f8475bd99b_24.jpg\",\"image_32\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2015-03-12\\/4026132781_fd82554431f8475bd99b_32.jpg\",\"image_48\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2015-03-12\\/4026132781_fd82554431f8475bd99b_48.jpg\",\"image_72\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2015-03-12\\/4026132781_fd82554431f8475bd99b_72.jpg\",\"image_192\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2015-03-12\\/4026132781_fd82554431f8475bd99b_192.jpg\",\"image_original\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2015-03-12\\/4026132781_fd82554431f8475bd99b_original.jpg\",\"real_name\":\"Mike Weiss\",\"real_name_normalized\":\"Mike Weiss\",\"email\":\"mlweiss10@gmail.com\"},\"is_admin\":false,\"is_owner\":false,\"is_primary_owner\":false,\"is_restricted\":false,\"is_ultra_restricted\":false,\"is_bot\":false},{\"id\":\"U033PNZ44\",\"name\":\"rprentki\",\"deleted\":false,\"status\":null,\"color\":\"d58247\",\"real_name\":\"Rachel Prentki\",\"tz\":\"America\\/Indiana\\/Indianapolis\",\"tz_label\":\"Eastern Daylight Time\",\"tz_offset\":-14400,\"profile\":{\"first_name\":\"Rachel\",\"last_name\":\"Prentki\",\"title\":\"Game Master\",\"real_name\":\"Rachel Prentki\",\"real_name_normalized\":\"Rachel Prentki\",\"email\":\"rprentki@eyewire.org\",\"image_24\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/8553cd2b8775b9e23730433388e9fc44.jpg?s=24&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0003-24.png\",\"image_32\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/8553cd2b8775b9e23730433388e9fc44.jpg?s=32&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F272a%2Fimg%2Favatars%2Fava_0003-32.png\",\"image_48\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/8553cd2b8775b9e23730433388e9fc44.jpg?s=48&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0003-48.png\",\"image_72\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/8553cd2b8775b9e23730433388e9fc44.jpg?s=72&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0003-72.png\",\"image_192\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/8553cd2b8775b9e23730433388e9fc44.jpg?s=192&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0003.png\"},\"is_admin\":false,\"is_owner\":false,\"is_primary_owner\":false,\"is_restricted\":false,\"is_ultra_restricted\":false,\"is_bot\":false},{\"id\":\"U02U8RKR3\",\"name\":\"shang\",\"deleted\":false,\"status\":null,\"color\":\"5b89d5\",\"real_name\":\"Shang Mu\",\"tz\":\"America\\/Indiana\\/Indianapolis\",\"tz_label\":\"Eastern Daylight Time\",\"tz_offset\":-14400,\"profile\":{\"first_name\":\"Shang\",\"last_name\":\"Mu\",\"real_name\":\"Shang Mu\",\"real_name_normalized\":\"Shang Mu\",\"email\":\"smu.synapse@gmail.com\",\"image_24\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/a9eba9154c48d9eee963a84a850bb3b6.jpg?s=24&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0021-24.png\",\"image_32\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/a9eba9154c48d9eee963a84a850bb3b6.jpg?s=32&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0021-32.png\",\"image_48\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/a9eba9154c48d9eee963a84a850bb3b6.jpg?s=48&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0021-48.png\",\"image_72\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/a9eba9154c48d9eee963a84a850bb3b6.jpg?s=72&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0021-72.png\",\"image_192\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/a9eba9154c48d9eee963a84a850bb3b6.jpg?s=192&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F272a%2Fimg%2Favatars%2Fava_0021.png\"},\"is_admin\":false,\"is_owner\":false,\"is_primary_owner\":false,\"is_restricted\":false,\"is_ultra_restricted\":false,\"is_bot\":false},{\"id\":\"U033TSX9A\",\"name\":\"sorek.m\",\"deleted\":false,\"status\":null,\"color\":\"53b759\",\"real_name\":\"M Sorek\",\"tz\":\"America\\/Indiana\\/Indianapolis\",\"tz_label\":\"Eastern Daylight Time\",\"tz_offset\":-14400,\"profile\":{\"first_name\":\"M\",\"last_name\":\"Sorek\",\"image_24\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2014-12-02\\/3130081378_41d1eb762fc8b31dd5f1_24.jpg\",\"image_32\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2014-12-02\\/3130081378_41d1eb762fc8b31dd5f1_32.jpg\",\"image_48\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2014-12-02\\/3130081378_41d1eb762fc8b31dd5f1_48.jpg\",\"image_72\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2014-12-02\\/3130081378_41d1eb762fc8b31dd5f1_72.jpg\",\"image_192\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2014-12-02\\/3130081378_41d1eb762fc8b31dd5f1_192.jpg\",\"image_original\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2014-12-02\\/3130081378_41d1eb762fc8b31dd5f1_original.jpg\",\"real_name\":\"M Sorek\",\"real_name_normalized\":\"M Sorek\",\"email\":\"m@eyewire.org\"},\"is_admin\":false,\"is_owner\":false,\"is_primary_owner\":false,\"is_restricted\":false,\"is_ultra_restricted\":false,\"is_bot\":false},{\"id\":\"U04EB26E0\",\"name\":\"stu\",\"deleted\":false,\"status\":null,\"color\":\"a2a5dc\",\"real_name\":\"Stu Holmes\",\"tz\":\"America\\/Indiana\\/Indianapolis\",\"tz_label\":\"Eastern Daylight Time\",\"tz_offset\":-14400,\"profile\":{\"first_name\":\"Stu\",\"last_name\":\"Holmes\",\"image_24\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2015-04-22\\/4553793110_990af0700e550b96468e_24.jpg\",\"image_32\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2015-04-22\\/4553793110_990af0700e550b96468e_32.jpg\",\"image_48\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2015-04-22\\/4553793110_990af0700e550b96468e_48.jpg\",\"image_72\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2015-04-22\\/4553793110_990af0700e550b96468e_72.jpg\",\"image_192\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2015-04-22\\/4553793110_990af0700e550b96468e_192.jpg\",\"image_original\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2015-04-22\\/4553793110_990af0700e550b96468e_original.jpg\",\"phone\":\"603-438-5539\",\"title\":\"Graphic designer\",\"real_name\":\"Stu Holmes\",\"real_name_normalized\":\"Stu Holmes\",\"email\":\"notgarystu@gmail.com\"},\"is_admin\":false,\"is_owner\":false,\"is_primary_owner\":false,\"is_restricted\":false,\"is_ultra_restricted\":false,\"is_bot\":false},{\"id\":\"U02T22LS0\",\"name\":\"tartavull\",\"deleted\":false,\"status\":null,\"color\":\"e7392d\",\"real_name\":\"Ignacio Tartavull\",\"tz\":\"America\\/Buenos_Aires\",\"tz_label\":\"Argentina Time\",\"tz_offset\":-10800,\"profile\":{\"first_name\":\"Ignacio\",\"last_name\":\"Tartavull\",\"image_24\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2014-11-02\\/2918609873_21e872287a4d3584917b_24.jpg\",\"image_32\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2014-11-02\\/2918609873_21e872287a4d3584917b_32.jpg\",\"image_48\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2014-11-02\\/2918609873_21e872287a4d3584917b_48.jpg\",\"image_72\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2014-11-02\\/2918609873_21e872287a4d3584917b_72.jpg\",\"image_192\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2014-11-02\\/2918609873_21e872287a4d3584917b_192.jpg\",\"image_original\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2014-11-02\\/2918609873_21e872287a4d3584917b_original.jpg\",\"title\":\"45 Park place, Princeton NJ 08542 \",\"skype\":\"\",\"phone\":\"(609) 356 - 2458\",\"real_name\":\"Ignacio Tartavull\",\"real_name_normalized\":\"Ignacio Tartavull\",\"email\":\"tartavull@princeton.edu\"},\"is_admin\":true,\"is_owner\":true,\"is_primary_owner\":false,\"is_restricted\":false,\"is_ultra_restricted\":false,\"is_bot\":false},{\"id\":\"U02TTRYS7\",\"name\":\"tmacrina\",\"deleted\":false,\"status\":null,\"color\":\"674b1b\",\"real_name\":\"Tommy Macrina\",\"tz\":\"America\\/Indiana\\/Indianapolis\",\"tz_label\":\"Eastern Daylight Time\",\"tz_offset\":-14400,\"profile\":{\"phone\":\"3152644105\",\"first_name\":\"Tommy\",\"last_name\":\"Macrina\",\"image_24\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2015-01-05\\/3337960248_cb88cbba7e737c015fe2_24.jpg\",\"image_32\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2015-01-05\\/3337960248_cb88cbba7e737c015fe2_32.jpg\",\"image_48\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2015-01-05\\/3337960248_cb88cbba7e737c015fe2_48.jpg\",\"image_72\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2015-01-05\\/3337960248_cb88cbba7e737c015fe2_72.jpg\",\"image_192\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2015-01-05\\/3337960248_cb88cbba7e737c015fe2_192.jpg\",\"image_original\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2015-01-05\\/3337960248_cb88cbba7e737c015fe2_original.jpg\",\"real_name\":\"Tommy Macrina\",\"real_name_normalized\":\"Tommy Macrina\",\"email\":\"tmacrina@princeton.edu\"},\"is_admin\":false,\"is_owner\":false,\"is_primary_owner\":false,\"is_restricted\":false,\"is_ultra_restricted\":false,\"is_bot\":false},{\"id\":\"U0320HC20\",\"name\":\"twister8484\",\"deleted\":false,\"status\":null,\"color\":\"4cc091\",\"real_name\":\"Doug Bland\",\"tz\":\"America\\/Indiana\\/Indianapolis\",\"tz_label\":\"Eastern Daylight Time\",\"tz_offset\":-14400,\"profile\":{\"first_name\":\"Doug\",\"last_name\":\"Bland\",\"real_name\":\"Doug Bland\",\"real_name_normalized\":\"Doug Bland\",\"email\":\"twister8484@gmail.com\",\"image_24\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/0bbbce1eceed154e18d162573ff63c6b.jpg?s=24&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0010-24.png\",\"image_32\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/0bbbce1eceed154e18d162573ff63c6b.jpg?s=32&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0010-32.png\",\"image_48\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/0bbbce1eceed154e18d162573ff63c6b.jpg?s=48&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0010-48.png\",\"image_72\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/0bbbce1eceed154e18d162573ff63c6b.jpg?s=72&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0010-72.png\",\"image_192\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/0bbbce1eceed154e18d162573ff63c6b.jpg?s=192&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0010.png\"},\"is_admin\":false,\"is_owner\":false,\"is_primary_owner\":false,\"is_restricted\":false,\"is_ultra_restricted\":false,\"is_bot\":false},{\"id\":\"U033RMUJH\",\"name\":\"wileykit\",\"deleted\":false,\"status\":null,\"color\":\"bb86b7\",\"real_name\":\"Kyle Willie\",\"tz\":\"America\\/Indiana\\/Indianapolis\",\"tz_label\":\"Eastern Daylight Time\",\"tz_offset\":-14400,\"profile\":{\"first_name\":\"Kyle\",\"last_name\":\"Willie\",\"image_24\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2014-12-23\\/3282832446_3013937cc45b8274118b_24.jpg\",\"image_32\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2014-12-23\\/3282832446_3013937cc45b8274118b_32.jpg\",\"image_48\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2014-12-23\\/3282832446_3013937cc45b8274118b_48.jpg\",\"image_72\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2014-12-23\\/3282832446_3013937cc45b8274118b_72.jpg\",\"image_192\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2014-12-23\\/3282832446_3013937cc45b8274118b_192.jpg\",\"image_original\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2014-12-23\\/3282832446_3013937cc45b8274118b_original.jpg\",\"real_name\":\"Kyle Willie\",\"real_name_normalized\":\"Kyle Willie\",\"email\":\"kylewillie85@gmail.com\"},\"is_admin\":false,\"is_owner\":false,\"is_primary_owner\":false,\"is_restricted\":false,\"is_ultra_restricted\":false,\"is_bot\":false},{\"id\":\"U02FH4TGY\",\"name\":\"will\",\"deleted\":true,\"profile\":{\"real_name\":\"\",\"real_name_normalized\":\"\",\"email\":\"will@eyewire.org\",\"image_24\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/fe8a276ff22be0372579c0a67cc79145.jpg?s=24&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0010-24.png\",\"image_32\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/fe8a276ff22be0372579c0a67cc79145.jpg?s=32&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0010-32.png\",\"image_48\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/fe8a276ff22be0372579c0a67cc79145.jpg?s=48&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0010-48.png\",\"image_72\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/fe8a276ff22be0372579c0a67cc79145.jpg?s=72&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0010-72.png\",\"image_192\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/fe8a276ff22be0372579c0a67cc79145.jpg?s=192&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0010.png\"}},{\"id\":\"U02U5UULA\",\"name\":\"william\",\"deleted\":false,\"status\":null,\"color\":\"684b6c\",\"real_name\":\"Will Silversmith\",\"tz\":\"America\\/Indiana\\/Indianapolis\",\"tz_label\":\"Eastern Daylight Time\",\"tz_offset\":-14400,\"profile\":{\"first_name\":\"Will\",\"last_name\":\"Silversmith\",\"real_name\":\"Will Silversmith\",\"real_name_normalized\":\"Will Silversmith\",\"email\":\"wms@mit.edu\",\"image_24\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/a54766f309325fa5ef5f7daa76900e2d.jpg?s=24&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0023-24.png\",\"image_32\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/a54766f309325fa5ef5f7daa76900e2d.jpg?s=32&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F272a%2Fimg%2Favatars%2Fava_0023-32.png\",\"image_48\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/a54766f309325fa5ef5f7daa76900e2d.jpg?s=48&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F272a%2Fimg%2Favatars%2Fava_0023-48.png\",\"image_72\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/a54766f309325fa5ef5f7daa76900e2d.jpg?s=72&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0023-72.png\",\"image_192\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/a54766f309325fa5ef5f7daa76900e2d.jpg?s=192&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0023.png\"},\"is_admin\":false,\"is_owner\":false,\"is_primary_owner\":false,\"is_restricted\":false,\"is_ultra_restricted\":false,\"is_bot\":false},{\"id\":\"U03404U57\",\"name\":\"zlateski\",\"deleted\":false,\"status\":null,\"color\":\"385a86\",\"real_name\":\"Aleksandar Zlateski\",\"tz\":\"America\\/Indiana\\/Indianapolis\",\"tz_label\":\"Eastern Daylight Time\",\"tz_offset\":-14400,\"profile\":{\"first_name\":\"Aleksandar\",\"last_name\":\"Zlateski\",\"real_name\":\"Aleksandar Zlateski\",\"real_name_normalized\":\"Aleksandar Zlateski\",\"email\":\"zlateski@mit.edu\",\"image_24\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/fe17360fcbd6424f9ea74d4f3c417adf.jpg?s=24&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0017-24.png\",\"image_32\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/fe17360fcbd6424f9ea74d4f3c417adf.jpg?s=32&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0017-32.png\",\"image_48\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/fe17360fcbd6424f9ea74d4f3c417adf.jpg?s=48&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0017-48.png\",\"image_72\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/fe17360fcbd6424f9ea74d4f3c417adf.jpg?s=72&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0017-72.png\",\"image_192\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/fe17360fcbd6424f9ea74d4f3c417adf.jpg?s=192&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0017.png\"},\"is_admin\":false,\"is_owner\":false,\"is_primary_owner\":false,\"is_restricted\":false,\"is_ultra_restricted\":false,\"is_bot\":false},{\"id\":\"USLACKBOT\",\"name\":\"slackbot\",\"deleted\":false,\"status\":null,\"color\":\"757575\",\"real_name\":\"Slack Bot\",\"tz\":null,\"tz_label\":\"Pacific Daylight Time\",\"tz_offset\":-25200,\"profile\":{\"first_name\":\"Slack\",\"last_name\":\"Bot\",\"image_24\":\"https:\\/\\/slack-assets2.s3-us-west-2.amazonaws.com\\/10068\\/img\\/slackbot_24.png\",\"image_32\":\"https:\\/\\/slack-assets2.s3-us-west-2.amazonaws.com\\/10068\\/img\\/slackbot_32.png\",\"image_48\":\"https:\\/\\/slack-assets2.s3-us-west-2.amazonaws.com\\/10068\\/img\\/slackbot_48.png\",\"image_72\":\"https:\\/\\/slack-assets2.s3-us-west-2.amazonaws.com\\/10068\\/img\\/slackbot_72.png\",\"image_192\":\"https:\\/\\/slack-assets2.s3-us-west-2.amazonaws.com\\/10068\\/img\\/slackbot_192.png\",\"real_name\":\"Slack Bot\",\"real_name_normalized\":\"Slack Bot\",\"email\":null},\"is_admin\":false,\"is_owner\":false,\"is_primary_owner\":false,\"is_restricted\":false,\"is_ultra_restricted\":false,\"is_bot\":false}],\"bots\":[{\"id\":\"B04G83E18\",\"name\":\"chat-status\",\"deleted\":false,\"icons\":{\"emoji\":\":telephone:\",\"image_64\":\"https:\\/\\/slack-assets2.s3-us-west-2.amazonaws.com\\/5504\\/img\\/emoji\\/260e.png\"}},{\"id\":\"B00\",\"name\":\"dropbox\",\"deleted\":false,\"icons\":{\"image_48\":\"https:\\/\\/slack.global.ssl.fastly.net\\/20653\\/img\\/services\\/dropbox_48.png\"}},{\"id\":\"B03781U6A\",\"name\":\"hangouts\",\"deleted\":false,\"icons\":{\"image_48\":\"https:\\/\\/slack.global.ssl.fastly.net\\/11591\\/img\\/services\\/hangouts_48.png\"}},{\"id\":\"B02TDD80B\",\"name\":\"incoming-webhook\",\"deleted\":false,\"icons\":{\"image_48\":\"https:\\/\\/slack.global.ssl.fastly.net\\/12078\\/img\\/services\\/incoming-webhook_48.png\"}},{\"id\":\"B03946BCP\",\"name\":\"New Relic\",\"deleted\":false,\"icons\":{\"image_48\":\"https:\\/\\/slack.global.ssl.fastly.net\\/21884\\/plugins\\/new_relic\\/assets\\/bot_48.png\"}},{\"id\":\"B03P0SSQL\",\"name\":\"raspberry\",\"deleted\":false,\"icons\":{\"image_48\":\"https:\\/\\/slack.global.ssl.fastly.net\\/12078\\/img\\/services\\/incoming-webhook_48.png\"}},{\"id\":\"B03PA147S\",\"name\":\"rtm-status\",\"deleted\":false,\"icons\":{\"emoji\":\":rocket:\",\"image_64\":\"https:\\/\\/slack-assets2.s3-us-west-2.amazonaws.com\\/5504\\/img\\/emoji\\/1f680.png\"}},{\"id\":\"B03AP3H9Z\",\"name\":\"twitter\",\"deleted\":false,\"icons\":{\"image_48\":\"https:\\/\\/slack.global.ssl.fastly.net\\/20653\\/img\\/services\\/twitter_48.png\"}},{\"id\":\"B02TAJ26B\",\"name\":\"github\",\"deleted\":true,\"icons\":{\"image_48\":\"https:\\/\\/slack.global.ssl.fastly.net\\/20653\\/img\\/services\\/github_48.png\"}}],\"svn_rev\":\"dev\",\"min_svn_rev\":99999,\"version_ts\":1430405258,\"min_version_ts\":1429207025,\"cache_version\":\"v7-dog\"}');
	
//-->
</script>			
			
		
	<!-- output_js "core" -->
<script type="text/javascript" src="https://slack.global.ssl.fastly.net/39f0/js/rollup-core_required.js" crossorigin="anonymous"></script>
<script type="text/javascript" src="https://slack.global.ssl.fastly.net/c212/js/libs/bootstrap_plastic.js" crossorigin="anonymous"></script>
<script type="text/javascript" src="https://slack.global.ssl.fastly.net/bf3b/js/libs/fastclick.js" crossorigin="anonymous"></script>
<script type="text/javascript" src="https://slack.global.ssl.fastly.net/8556/js/libs/headroom.js" crossorigin="anonymous"></script>
<script type="text/javascript" src="https://slack.global.ssl.fastly.net/4a49/js/plastic.js" crossorigin="anonymous"></script>
<script type="text/javascript" src="https://slack.global.ssl.fastly.net/5b99/js/TS.web.js" crossorigin="anonymous"></script>

			<!-- output_js "secondary" -->
<script type="text/javascript" src="https://slack.global.ssl.fastly.net/b179/js/rollup-secondary_required.js" crossorigin="anonymous"></script>
<script type="text/javascript" src="https://slack.global.ssl.fastly.net/33c4/js/TS.storage.js" crossorigin="anonymous"></script>

		<!-- output_js "regular" -->
<script type="text/javascript" src="https://slack.global.ssl.fastly.net/fdb7/js/TS.web.comments.js" crossorigin="anonymous"></script>
<script type="text/javascript" src="https://slack.global.ssl.fastly.net/80ad/js/TS.web.file.js" crossorigin="anonymous"></script>
<script type="text/javascript" src="https://slack.global.ssl.fastly.net/2eab/js/libs/codemirror.js" crossorigin="anonymous"></script>
<script type="text/javascript" src="https://slack.global.ssl.fastly.net/9e78/js/codemirror_load.js" crossorigin="anonymous"></script>

		<script type="text/javascript">
	<!--
		boot_data.page_needs_custom_emoji = true;
		
		boot_data.file = JSON.parse('{\"id\":\"F04LGDKJM\",\"created\":1430406975,\"timestamp\":1430406975,\"name\":\"h52vast.py\",\"title\":\"h52vast.py\",\"mimetype\":\"text\\/plain\",\"filetype\":\"python\",\"pretty_type\":\"Python\",\"user\":\"U033T4SHE\",\"editable\":true,\"size\":855,\"mode\":\"snippet\",\"is_external\":false,\"external_type\":\"\",\"is_public\":false,\"public_url_shared\":false,\"url\":\"https:\\/\\/slack-files.com\\/files-pub\\/T02FH1DRA-F04LGDKJM-25f41f59ca\\/h52vast.py\",\"url_download\":\"https:\\/\\/slack-files.com\\/files-pub\\/T02FH1DRA-F04LGDKJM-25f41f59ca\\/download\\/h52vast.py\",\"url_private\":\"https:\\/\\/files.slack.com\\/files-pri\\/T02FH1DRA-F04LGDKJM\\/h52vast.py\",\"url_private_download\":\"https:\\/\\/files.slack.com\\/files-pri\\/T02FH1DRA-F04LGDKJM\\/download\\/h52vast.py\",\"permalink\":\"https:\\/\\/eyewire.slack.com\\/files\\/bun\\/F04LGDKJM\\/h52vast.py\",\"permalink_public\":\"https:\\/\\/slack-files.com\\/T02FH1DRA-F04LGDKJM-25f41f59ca\",\"edit_link\":\"https:\\/\\/eyewire.slack.com\\/files\\/bun\\/F04LGDKJM\\/h52vast.py\\/edit\",\"preview\":\"# -*- coding: utf-8 -*-\\n\\\"\\\"\\\"\\nCreated on Wed Mar 11 16:18:34 2015\\n\\n@author: jingpeng\\n\\\"\\\"\\\"\\n#%% parameters\\nimport numpy as np\\n\\nDir = \'\\/usr\\/people\\/bds2\\/seungmount\\/Omni\\/TracerTasks\\/Piriform_cortex_Corrections\\/Chunk_07\\/Chunk_07_EM\\/\'\",\"preview_highlight\":\"<div class=\\\"sssh-code\\\"><div class=\\\"sssh-line\\\"><pre><span class=\\\"sssh-comment\\\"># -*- coding: utf-8 -*-<\\/span><\\/pre><\\/div>\\n<div class=\\\"sssh-line\\\"><pre><span class=\\\"sssh-string\\\">&quot;&quot;&quot;<\\/pre><\\/div>\\n<div class=\\\"sssh-line\\\"><pre>Created on Wed Mar 11 16:18:34 2015<\\/pre><\\/div>\\n<div class=\\\"sssh-line\\\"><pre><\\/pre><\\/div>\\n<div class=\\\"sssh-line\\\"><pre>@author: jingpeng<\\/pre><\\/div>\\n<div class=\\\"sssh-line\\\"><pre>&quot;&quot;&quot;<\\/span><\\/pre><\\/div>\\n<div class=\\\"sssh-line\\\"><pre><span class=\\\"sssh-comment\\\">#%% parameters<\\/span><\\/pre><\\/div>\\n<div class=\\\"sssh-line\\\"><pre><span class=\\\"sssh-keyword\\\">import<\\/span> numpy <span class=\\\"sssh-keyword\\\">as<\\/span> np<\\/pre><\\/div>\\n<div class=\\\"sssh-line\\\"><pre><\\/pre><\\/div>\\n<div class=\\\"sssh-line\\\"><pre>Dir <span>=<\\/span> <span class=\\\"sssh-string\\\">\'\\/usr\\/people\\/bds2\\/seungmount\\/Omni\\/TracerTasks\\/Piriform_cortex_Corrections\\/Chunk_07\\/Chunk_07_EM\\/\'<\\/span><\\/pre><\\/div>\\n<\\/div>\",\"lines\":36,\"lines_more\":26,\"channels\":[],\"groups\":[],\"ims\":[\"D034A3B8R\"],\"comments_count\":0}');
		boot_data.file.comments = JSON.parse('[]');

		

		var g_editor;

		$(function(){

			var wrap_long_lines = !!TS.model.code_wrap_long_lines;

			g_editor = CodeMirror(function(elt){
				var content = document.getElementById("file_contents");
				content.parentNode.replaceChild(elt, content);
			}, {
				value: $('#file_contents').text(),
				lineNumbers: true,
				matchBrackets: true,
				indentUnit: 4,
				indentWithTabs: true,
				enterMode: "keep",
				tabMode: "shift",
				viewportMargin: Infinity,
				readOnly: true,
				lineWrapping: wrap_long_lines
			});

			$('#file_preview_wrap_cb').bind('change', function(e) {
				TS.model.code_wrap_long_lines = $(this).prop('checked');
				g_editor.setOption('lineWrapping', TS.model.code_wrap_long_lines);
			})

			$('#file_preview_wrap_cb').prop('checked', wrap_long_lines);

			CodeMirror.switchSlackMode(g_editor, 'python');
		});

		
		$('#file_comment').css('overflow', 'hidden').autogrow();
	//-->
	</script>

			<script type="text/javascript">TS.boot(boot_data);</script>
	<!-- slack-www268 / 2015-04-30 08:17:24 / v76609d9e04fa84ae39a5e2468b2f6f61492dac29 -->

</body>
</html>