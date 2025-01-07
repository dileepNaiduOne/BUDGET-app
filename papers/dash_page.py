import streamlit as st


with open( "style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

c1, c2, c3 = st.columns([1, 6, 1])

with c2:
    
    st.components.v1.html('''
        <div class='tableauPlaceholder' id='viz1735665238061' style='position: relative'>
            <noscript>
                <a href='#'><img alt='0 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;ch&#47;charts_17356651247130&#47;0&#47;1_rss.png' style='border: none' /></a>
            </noscript>
            <object class='tableauViz'  style='display:none;'>
                <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> 
                <param name='embed_code_version' value='3' /> 
                <param name='site_root' value='' />
                <param name='name' value='charts_17356651247130&#47;0' />
                <param name='tabs' value='no' />
                <param name='toolbar' value='yes' />
                <param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;ch&#47;charts_17356651247130&#47;0&#47;1.png' /> 
                <param name='animate_transition' value='yes' />
                <param name='display_static_image' value='yes' />
                <param name='display_spinner' value='yes' />
                <param name='display_overlay' value='yes' />
                <param name='display_count' value='yes' />
                <param name='language' value='en-US' />
            </object>
        </div>                
        
        <script type='text/javascript'>                    
            var divElement = document.getElementById('viz1735665238061');                    
            var vizElement = divElement.getElementsByTagName('object')[0];                    
            if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1366px';vizElement.style.height='795px';} 
            else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1366px';vizElement.style.height='795px';} 
            else { vizElement.style.width='100%';vizElement.style.height='1127px';}                    
            var scriptElement = document.createElement('script');                    
            scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    
            vizElement.parentNode.insertBefore(scriptElement, vizElement);                
        </script>
    ''', width=1500, height=800)

    st.link_button(label="View this chart on Tableau Public", url="https://public.tableau.com/views/charts_17356651247130/0?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link", type="primary")
    b1 = st.button(label="Back to Home", type="primary")
    if b1:
        st.switch_page("papers/home_page.py")