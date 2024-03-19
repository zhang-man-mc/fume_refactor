empty_html = """
<!DOCTYPE html>
<html>
  <head>
    <title>油烟系统-油烟数据</title>
	<meta http-equiv="pragma" content="no-cache"/>
	<meta http-equiv="cache-control" content="no-cache"/>
	<meta http-equiv="expires" content="0"/>    
	<meta name="robots" content="nofollow" />
	<link href="../css/jquery-ui/jquery-ui-1.10.4.custom.min.css" rel="stylesheet" type="text/css" />
	<link href="../css/sys.css" rel="stylesheet" type="text/css" />
	<script type="text/javascript" src="../js/jquery-3.6.0.min.js"></script><script type="text/javascript" src="../js/jquery-migrate-3.3.2.min.js"></script>
	<script type="text/javascript" src="../js/jquery-ui-1.10.4.custom.min.js"></script>
	<script type="text/javascript" src="../js/sys.js"></script>
	<script type="text/javascript" src="../js/work.js"></script>
<script type="text/javascript">
	page_url="yyRealTimeValue_list.jsp";
	link1_name="油烟系统",link2_name="油烟数据",link2_url="yyRealTimeValue_list.jsp";
</script>
 </head>
<body>

<div class="clear">
	<select id="sel_area" class="float_l border_b" style="width:140px;margin-top:8px;margin-left:5px;" onchange="dataResift('area',$(this).val())">
		<option value="all">全部地区</option>
		
			<option value='785' >徐汇区</option>
		
			<option value='3888' >徐家汇街道</option>
		
			<option value='3889' >湖南路街道</option>
		
			<option value='3890' >天平路街道</option>
		
			<option value='3891' >枫林路街道</option>
		
			<option value='3892' >斜土路街道</option>
		
			<option value='3894' >康健新村街道</option>
		
			<option value='3895' >虹梅路街道</option>
		
			<option value='3896' >田林街道</option>
		
			<option value='3897' >凌云路街道</option>
		
			<option value='3898' >龙华街道</option>
		
			<option value='3899' >华泾镇</option>
		
			<option value='3903' >漕河泾新兴技术开发区</option>
		
			<option value='3893' >长桥街道</option>
		
			<option value='3900' >漕河泾街道</option>
		
	</select>
	<select id="sel_supplier" class="float_l border_b" style="margin-top:8px;margin-left:5px;" onchange="dataResift('supplier',$(this).val())">
		<option value="all">全部供应商</option>
	
			<option value='1' >供应商公用调试</option>
	
			<option value='2' >开发公司调试帐号</option>
	
			<option value='3' >上海广聆环保科技</option>
	
			<option value='5' >上海政宝环保科技</option>
	
			<option value='7' >上海中映信息科技</option>
	
			<option value='8' >上海富程环保工程</option>
	
			<option value='9' >上海勤世环保科技</option>
	
			<option value='10' >上海卓荃电子科技</option>
	
			<option value='11' >衡智远科技（深圳）</option>
	
			<option value='12' >无锡锐丰源环境科技</option>
	
			<option value='13' >上海龙涤环保技术工程</option>
	
			<option value='14' >上海辉瀚环保科技</option>
	
			<option value='15' >上海景瑄环保科技</option>
	
			<option value='16' >上海叶榕环保设备工程</option>
	
			<option value='17' >山东威盟士科技</option>
	
			<option value='18' >上海茂净环境科技</option>
	
			<option value='19' >上海汇星辰餐饮</option>
	
			<option value='20' >北京万维盈创科技发展</option>
	
			<option value='21' >埃尔斯虏森空气净化系统(上海)</option>
	
			<option value='22' >上海厨亦安设备安装工程</option>
	
	</select>
	<select class="float_l border_b" style="margin-top:8px;margin-left:5px;" onchange="dataResift('idx',$(this).val())">
		<option value="all">全部级别</option>
		<option value="0" >未定义</option>
		<option value="1" >优</option>
		<option value="2" >良</option>
		<option value="3" >中</option>
		<option value="4" >差</option>
	</select>
	<span class="float_l" style="margin-top:6px;margin-left:5px;">需警报：</span>
	<select class="float_l border_b" style="margin-top:8px;" onchange="dataResift('needAlarm',$(this).val())">
		<option value="all">全部</option>
		<option value="1" >是</option>
		<option value="0" >否</option>
	</select>
	<span class="float_l" style="margin-top:6px;margin-left:5px;">已警报：</span>
	<select class="float_l border_b" style="margin-top:8px;" onchange="dataResift('hasAlarm',$(this).val())">
		<option value="all">全部</option>
		<option value="1" >是</option>
		<option value="0" >否</option>
	</select>
	<div class="float_l" style="margin-top:6px;margin-left:5px;">
		<input type="text" class="border_b input_date" id="date1" style="width:85px;position:relative;" value="2024-03-01" readonly="readonly"/>
		-
		<input type="text" class="border_b input_date" id="date2" style="width:85px;position:relative;" value="2024-03-18" readonly="readonly"/>
		&nbsp;
		<a class='cur_poi blue2' onclick="goDateRange('2024-02-01','2024-02-29')" title="2024-02-01~2024-02-29">上月</a>
		&nbsp;
		<a class='cur_poi blue2' onclick="goDateRange('2024-03-11','2024-03-17')" title="2024-03-11~2024-03-17">上周</a>
		&nbsp;
		<a class='cur_poi blue2' onclick="goDateRange('2024-03-01','2024-03-18')" title="2024-04-01~2024-04-30">本月</a>
		&nbsp;
		<a class='cur_poi blue2' onclick="goDateRange('2024-03-25','2024-03-31')" title="2024-03-25~2024-03-31">下周</a>
		&nbsp;
		<a class='cur_poi blue2' onclick="goDateRange('2024-04-01','2024-04-30')" title="2024-04-01~2024-04-30">下月</a>
	</div>
	<div class="float_r" style="margin-right:5px;margin-top:6px;">
		<span class="float_l" style="margin-left:5px;">店名：</span>
		<input id="shop" class="border_b float_l" style="width:100px;height:22px;" value="食其家"/>
		<span class="float_l" style="margin-left:5px;">设备编号：</span>
		<input id="key1" class="border_b float_l" style="border-right:0px;width:100px;height:22px;" value=""/>
		<input type="button" class="float_l bg_blue4 color_f" style="width:50px;height:24px;border:0px;" value="搜 索" onclick="dataRefind2()"/>
		<div class="clear"></div>
	</div>
	<div class="clear"></div>
</div>
<table class="table_1" style="clear:both;margin-top:5px;">
	<tr class="tr_head">
		<td>地区</td>
		<td>餐饮店/地址</td>
		<td>设备编号/供应商</td>
		<td style="width:70px;">进烟浓度<br/>mg/m³</td>
		<td style="width:70px;">排烟浓度<br/>mg/m³</td>
		<td style="width:60px;">风机电<br/>A</td>
		<td style="width:60px;">净化器<br/>A</td>
		<td style="width:50px;">级别</td>
		<td style="width:50px;">需报警</td>
		<td style="width:50px;">已报警</td>
		<td style="width:140px;">归属时段<br/>上报时间</td>
	    <td style="width:100px;" colspan='2'>基本操作</td>
	</tr>
<tbody>

</tbody>
</table>
<div class='bg_e align_c' style='padding:30px;'>暂无数据</div>
<div class='clear align_r color_2' style="margin-top:5px;font-size:14px">
	<input type="button" class='bg_green5 color_f border_d' style="height:24px;width:200px;" value="导出当前搜索条件的全部结果" onclick="dataExcel()"/>
	<span>
	<a class='cur_poi' onclick='gotoPage(1)'>上一页</a>&nbsp;&nbsp;[2]&nbsp;&nbsp;
		第<input id='page' class="border_b" style='width:40px;height:18px;margin-bottom:-1px;margin-left:2px;margin-right:2px;'/>页 <input type='button' class="bg_2 color_f" style='width:30px;height:22px;font-size:12px;' value='Go' onclick='gotoPage()'/>
	</span>
	<select id="sel_pageSize" class="border_b" style="width:80px;" onchange="dataResift('pagesize',$(this).val())">
		<option value="10">10条/页</option>
		<option value="20">20条/页</option>
		<option value="50">50条/页</option>
		<option value="100">100条/页</option>
	</select>
</div>
<div id="shadow" style="z-index:900;display:none;position:fixed;left:0px;top:0px;right:0px;bottom:0px;background-color:#000000;opacity:0.3;filter:alpha(opacity=30);"></div>
<div id="working" class="positionable absolute align_c" style="z-index:999;display:none;border:1px solid #84A0C4;background-color:#ffffff;width:300px;padding:40px 0px">
	<img alt='请稍候' src="../image/pub/working.gif"/>
</div>

  </body>
</html>
"""
