import ipywidgets as widgets
import traitlets


@widgets.register('animation.Animation')
class AnimationWidget(widgets.DOMWidget):
    """
    A widget that periodic increment a value

    :param value: A float between 0 and 1
    :param run: boolean with the state of the timer. True, the timer is enable

    Produces the following signal. A sampling rate, the value is interpolated
    with the equation val = 1/Period * t
    1- ^  ____
       | /
       |/
    0- |----->
          |
        period 
    """
    _view_name = traitlets.Unicode('AnimationView').tag(sync=True)
    _model_name = traitlets.Unicode('AnimationModel').tag(sync=True)
    _view_module = traitlets.Unicode('animation-widget').tag(sync=True)
    _model_module = traitlets.Unicode('animation-widget').tag(sync=True)
    value = traitlets.CFloat(0.0).tag(sync=True)
    run = traitlets.CBool(False).tag(sync=True)

