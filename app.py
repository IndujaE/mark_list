from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/')
def indexfunc():
    return render_template('index.html')

@app.route('/create')
def createfunc():
    return render_template('create.html')


@app.route('/glist',methods=['GET','POST'])
def glistfunc():
    if(request.method=='POST'):
        getname=(request.form['name'])
        getrno=request.form['regno']
        getsem=request.form['sem']
        getcname=request.form['cname']

        getsub1=request.form['subj1']
        getmark1=int(request.form['mark1'])
        gettm1=int(request.form['tmark1'])

        getsub2=request.form['subj2']
        getmark2=int(request.form['mark2'])
        gettm2=int(request.form['tmark2'])

        getsub3=request.form['subj3']
        getmark3=int(request.form['mark3'])
        gettm3=int(request.form['tmark3'])

        getsub4=request.form['subj4']
        getmark4=int(request.form['mark4'])
        gettm4=int(request.form['tmark4'])

        def grade(percent):
                if(percent>=90):
                        return 'A'
                elif(percent>=80):
                        return 'B'
                elif(percent>=70):
                        return 'C'
                elif(percent>=60):
                        return 'D'
                else:
                        return 'F'

        
        p1=(float(getmark1)/float(gettm1))*100
        p2=(float(getmark2)/float(gettm2))*100
        p3=(float(getmark3)/float(gettm3))*100
        p4=(float(getmark4)/float(gettm4))*100 

        g1=grade(p1)
        g2=grade(p2)
        g3=grade(p3)
        g4=grade(p4)

        if((g1!='F')and(g2!='F')and(g3!='F')and(g4!='F')):
                status=" Passed...Congratulations"
        else:
                status=" Failed...Better luck next time"


        return render_template('mlist.html', getname=getname,getrno=getrno,getsem=getsem,getcname=getcname,getsub1=getsub1,getmark1=getmark1,gettm1=gettm1,getsub2=getsub2,getmark2=getmark2,gettm2=gettm2,getsub3=getsub3,getmark3=getmark3,gettm3=gettm3,getsub4=getsub4,getmark4=getmark4,gettm4=gettm4,g1=g1,g2=g2,g3=g3,g4=g4,status=status)

  



if(__name__=='__main__'):
    app.run(debug=True)


