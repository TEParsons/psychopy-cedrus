from psychopy.experiment.components.buttonBox import ButtonBoxBackend, ButtonBoxComponent
from psychopy.experiment import getInitVals, Param
from psychopy.localization import _translate


class RipondaButtonBoxBackend(ButtonBoxBackend, key="riponda", label="Cedrus Riponda"):
    """
    Adds a basic serial connection backend for ButtonBoxComponent, as well as acting as an example for implementing
    other ButtonBoxBackends.
    """

    def getParams(self: ButtonBoxComponent):
        # define order
        order = [
            "ripondaIndex",
        ]
        # define params
        params = {}
        params['ripondaIndex'] = Param(
            0, valType='int', inputType="single", categ='Device',
            label=_translate("Baud rate"),
            hint=_translate(
                "Device number, if you have multiple devices which one do you want (0, 1, 2...)"
            )
        )
        return params, order

    def addRequirements(self: ButtonBoxComponent):
        self.exp.requireImport(
            importName="riponda", importFrom="psychopy_cedrus"
        )

    def writeInitCode(self: ButtonBoxComponent, buff):
        # get inits
        inits = getInitVals(self.params)
        # make Keyboard object
        code = (
            "%(name)s = riponda.RipondaButtonGroup(\n"
            "    pad=%(ripondaIndex)s\n"
            ")\n"
        )
        buff.writeIndentedLines(code % inits)