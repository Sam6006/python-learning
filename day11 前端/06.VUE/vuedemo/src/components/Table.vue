<template>
    <div class="warpper">
      <table class="table">
      <tr>
        <td colspan="4" class="header-line"><el-button type="info"><span @click="show_form">添加数据</span></el-button></td>
      </tr>
        <tr>
          <th>日期</th>
          <th>姓名</th>
          <th>地址</th>
          <th>操作</th>
        </tr>
        <tr v-for="data, key in tableData">
          <td>{{data.date}}</td>
          <td>{{data.name}}</td>
          <td>{{data.address}}</td>
          <td><el-button type="danger"><span @click="del_data(key)">删除</span></el-button></td>
        </tr>
      </table>
          <el-dialog title="个人信息" :visible.sync="dialogFormVisible">
      <el-form :model="form">
        <el-form-item label="姓名" >
          <el-input v-model="form.name" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="日期" >
          <el-input v-model="form.date" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="地址" >
          <el-input v-model="form.address" autocomplete="off"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="save_data">确 定</el-button>
      </div>
    </el-dialog>
    </div>
</template>

<script>
  export default {
    name: 'Table',
    data() {
      return {
        form:{
            name:'',
            date:'',
            address: '',
        },
        dialogFormVisible: false,
        tableData: [{
          date: '2016-05-02',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1518 弄'
        }, {
          date: '2016-05-04',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1517 弄'
        }, {
          date: '2016-05-01',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1519 弄'
        }, {
          date: '2016-05-03',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1516 弄'
        }],
      }
    },
    methods:{
        del_data(key){
          this.$confirm('此操作将永久删除该文件, 是否继续?', '温馨提示', {
            confirmButtonText: '删除',
            cancelButtonText: '取消',
            type: 'warning'
          }).then(() => {
              //确定删除
            this.tableData.splice(key,1);
            this.$message({
              type: 'success',

              message: '删除成功!'
            });
          }).catch(() => {
            //取消
          });
      },
        show_form(){
          this.dialogFormVisible = true;
        },
        save_data(){
          this.tableData.push({
            name:this.form.name,
            date: this.form.date,
            address: this.form.address,
          });
            this.dialogFormVisible = false;
            this.form.date = '';
            this.form.name = '';
            this.form.address = ''
        }
    }
  }
</script>

<style scoped>
.table{
  width:800px!important;
  margin: 0 auto;
  border-collapse: collapse; /*合并边框*/
}
  .table th{
    font-weight: normal;
  }
  .table td{
    text-align: center;
  }

  .table tr td{
    height: 42px;
    line-height: 42px;
    border-bottom: 1px solid blanchedalmond;
  }
  tr .header-line{
    text-align: left;
  }
</style>
