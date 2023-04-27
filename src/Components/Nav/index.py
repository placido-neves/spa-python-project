from dom.compy import Component

com = Component()

style = com.staticFile('src/Components/Nav/style.css')

@com.compy(css=style)
def Nav():
    return f"""
        <nav>
            <i class="fa-brands fa-github"></i> 
                <input
                    className='text'
                    value=""
                    onChange=""
                    placeholder=""
                />
                <button type="submit" className='bntSeach'>seach</button>
        </nav> 
        <h1>ola mundo</h1>            
    """ 